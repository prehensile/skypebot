import time
import pkgutil
import datetime
import json
import sys
import logging
import twitterconnector
from hookserver import HookServerMessage, HookServerThread
import queuedthread
import time
from messages import housekeeping, streetnoise
import re
import os
import commands
import urllib2
import urllib
import skypeconnector

RUN_SKYPE = True
ENABLE_TWITTER = True
ENABLE_GIFTS = True
ENABLE_RADIO = True
ENABLE_API = True
class BotThread( queuedthread.QueuedThread ):
    
    def __init__( self ):
        global ENABLE_RADIO, ENABLE_API        
        self.twitter_connector = None
        self.radio_url = None
        if ENABLE_RADIO:
            try:
                fh = open( "radio_url")
                self.radio_url = fh.readline().rstrip()
                fh.close()
                logging.info( "Loaded radio_url: %s", self.radio_url ) 
            except IOError, e:
                ENABLE_RADIO = False        
        if ENABLE_API:
            self.api_server = HookServerThread()
            self.api_server.portnumber = 9666
            self.api_server.start()
        super( BotThread, self ).__init__()

    def send_radio( self, message, id ):
        if self.radio_url is not None:
            if message.startswith( "/me" ):
                message = message[3:]
                message = message.lstrip()
            data = dict( id=id, line=message )
            f = urllib.urlopen( self.radio_url, urllib.urlencode(data) )
            resp = f.read() # force read

    def stop( self, message=None ):
        if self.twitter_connector:
            self.twitter_connector.stop()
        if message is not None:
            self.message_all( message )
        super( BotThread, self ).stop()

    def run( self ):
        self._abortflag = False
        
        # twitter connection
        if ENABLE_TWITTER:
            logging.info( "Starting up Twitter connector..." )
            self.twitter_connector = twitterconnector.TwitterConnectorThread()
            self.twitter_connector.creds_path = "twitter_creds"
            self.twitter_connector.track_keywords = ["lndlrd"]
            self.twitter_connector.start()

        # import commands
        all_commands = []
        logging.info( "Loading commands..." )
        ## load all commands
        reload( commands )
        for loader, modname, ispkg in pkgutil.iter_modules( commands.__path__, prefix="commands." ):
            try:
                logging.info( "Scan module: %s" % modname)
                module = __import__( modname, fromlist="dummy" )
                reload( module )
                for klassname in dir( module ):
                    if "Command" in klassname and "BaseCommand" not in klassname:
                        logging.info( "...instantiate command: %s" % klassname )
                        try:
                            kommandklass = getattr( module, klassname )
                            kommand = kommandklass()
                            all_commands.append( kommand )
                            logging.info( "......instantiated. Triggers are %s" % kommand.command_mappings )
                        except Exception, e:
                            logging.info( e )    
            except Exception, e:
                logging.info( e )
        logging.info( "Loaded %d commands." % len(all_commands) )

        if RUN_SKYPE:
            self.skype_connector = skypeconnector.SkypeConnector()
        
        logging.info( "Entering main run loop..." )
        while not self._abortflag:
            try:
                if RUN_SKYPE:
                    
                    # update chats
                    chat_handlers = self.skype_connector.update_chats()

                    for chat_name in chat_handlers:
                        chat_handler = chat_handlers[ chat_name ]
                        new_messages = chat_handler.update()
                        if len(new_messages)> 0:
                            print "New messages in chat: %s" % chat_handler.chat.FriendlyName
                        for new_message in new_messages:
                            body = new_message.Body
                            print body
                            bl = body.lower()
                            for command in all_commands:
                                try:
                                    if command.enabled:
                                        message_out = None
                                        for commandstring in command.command_mappings:
                                            commandbang = "!" + commandstring
                                            commandhash = "#" + commandstring
                                            if commandbang in bl or commandhash in bl:
                                                print "Excute command %s" % commandstring
                                                # if command is giftable
                                                if command.gifting_enabled and ENABLE_GIFTS:
                                                    if hasattr( command, 'gift' ):
                                                        # split message up into tokens
                                                        tokens = re.split( '\W+', body )
                                                        print tokens
                                                        if len( tokens ) > 1:
                                                            members = chat_handler.chat.Members
                                                            # scan tokens for something that looks like a name
                                                            for token in tokens:
                                                                if len(token) > 3 and token != commandstring:
                                                                    for member in members:
                                                                        names = [ member.DisplayName, member.FullName, member.Handle ]
                                                                        for name in names:
                                                                            if token.lower() in name.lower():
                                                                                print "-->  gift %s to %s " % (commandbang, name )
                                                                                message_out = command.gift( name )
                                                                                break
                                                                        if message_out is not None:
                                                                            break
                                                                if message_out is not None:
                                                                        break
                                                if message_out is None:
                                                    message_out = command.execute( new_message )

                                        if message_out is not None:
                                            chat_handler.chat.SendMessage( message_out )
                                            if ENABLE_TWITTER and command.tweets:
                                                self.twitter_connector.tweet( message_out )
                                            if ENABLE_RADIO:
                                                self.send_radio( message_out, new_message.Id )

                                except Exception, e:
                                    logging.info( e )
                                    print e
                    
                    # update from twitter
                    if ENABLE_TWITTER:
                        new_statuses = self.twitter_connector.pop_stream()
                        for status_in in new_statuses:
                            try:
                                message_out = streetnoise.message_for_incoming_status( status_in )
                                if message_out:
                                    self.message_all( message_out )
                                    if ENABLE_RADIO:
                                        self.send_radio( message_out, status_in.id_str )
                            except Exception, e:
                                logging.info( e )

                    # update from api
                    if ENABLE_API:
                        api_message = self.api_server.pop_message()
                        if api_message is not None:
                            try:
                                message_out = api_message.payload["message"]
                                self.message_all( message_out )
                            except Exception, e:
                                logging.info( e )
                    time.sleep(1)
            except Exception, e:
                logging.info( e )
                print e

        if ENABLE_TWITTER:
            self.twitter_connector.stop()
        if ENABLE_API:
            self.api_server.stop()    
