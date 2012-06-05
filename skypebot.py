import Skype4Py
import time
from commands import drinkcommand, wetcommand, baconcommand, snackcommand, \
cheesecommand, cockcommand, smokecommand, chooncommand, tvcommand, \
birthdaycommand, commandscratch, eurovisioncommand, teacommand, \
coffeecommand, satancommand, marcuscommand, byecommand, haicommand, \
poveycommand, rumblecommand
import datetime
import json
import sys
import logging
import twitterconnector
from hookserver import HookServerMessage
import queuedthread
import time
from messages import housekeeping

class ChatHandler(object):
    
    def __init__( self, Chat ):
        self.chat = Chat
        self.last_timestamp = datetime.datetime.now()

    def update( self ):
        new_messages = []
        messages = self.chat.RecentMessages
        for message in messages:
            dt = message.Datetime
            if dt > self.last_timestamp:
                new_messages.append( message )
                self.last_timestamp = dt
        return new_messages

RUN_SKYPE=True
class BotThread( queuedthread.QueuedThread ):
    
    def message_all( self, message ):
    # send message to all connected chats   
        for chat_name in self.chat_handlers:
            chat_handler = self.chat_handlers[ chat_name ]
            try:
                chat_handler.chat.SendMessage( message )
            except Exception, e:
                logging.info( e )

    def stop( self, message=None ):
        if message is not None:
            self.message_all( message )
        super( BotThread, self ).stop()

    def run( self ):
        self._abortflag = False
        
        # twitter connection
        logging.info( "Starting up Twitter connector..." )
        tw = twitterconnector.TwitterConnector( "twitter_creds" )

        # set up command handlers
        self.chat_handlers = {}
        command_mappings = {}
        command_mappings[ "drink" ] = drinkcommand.DrinkCommand()
        command_mappings[ "w3t" ] = wetcommand.WetCommand()
        command_mappings[ "bacon" ] = baconcommand.BaconCommand()
        command_mappings[ "snack" ] = snackcommand.SnackCommand()
        command_mappings[ "cheese" ] = cheesecommand.CheeseCommand()
        #command_mappings[ "cock" ] = cockcommand.CockCommand()
        command_mappings[ "choon" ] = chooncommand.ChoonCommand()
        command_mappings[ "smoke" ] = smokecommand.SmokeCommand()
        command_mappings[ "telly" ] = tvcommand.TVCommand()
        command_mappings[ "birthday" ] = birthdaycommand.BirthdayCommand()
        command_mappings[ "eurovision" ] = eurovisioncommand.EurovisionCommand()
        command_mappings[ "tea" ] = teacommand.TeaCommand()
        command_mappings[ "tv" ] = tvcommand.TVCommand()
        command_mappings[ "coffee" ] = coffeecommand.CoffeeCommand()
        command_mappings[ "satan" ] = satancommand.SatanCommand()
        command_mappings[ "marcus" ] = marcuscommand.MarcusCommand()
        command_mappings[ "bye" ] = byecommand.ByeCommand()
        command_mappings[ "hai" ] = haicommand.HaiCommand()
        command_mappings[ "ohai" ] = haicommand.HaiCommand()
        command_mappings[ "povey" ] = poveycommand.PoveyCommand()
        command_mappings[ "mullet"] = satancommand.MulletCommand()
        command_mappings[ "hat"] = commandscratch.HatCommand()
        command_mappings[ "brawl"] = rumblecommand.RumbleCommand()
        command_mappings[ "rumble"] = rumblecommand.RumbleCommand()


        if RUN_SKYPE:
            logging.info( "Attaching to Skype..." )
            skype = Skype4Py.Skype(Transport='x11')
            skype.Attach()
        
        logging.info( "Entering main run loop..." )
        while not self._abortflag:
            try:
                if RUN_SKYPE:
                    # maintain list of chats
                    chats = skype.ActiveChats
                    for chat in chats:
                        chat_name = chat.Name
                        if chat_name not in self.chat_handlers:
                            logging.info( "New handler for chat: %s" % chat.FriendlyName )
                            self.chat_handlers[chat_name] = ChatHandler(chat)
                            message = housekeeping.new_chat_message()
                            try:
                                chat.SendMessage( message )
                            except Exception, e:
                                logging.info( e )
                                print e

                    # TODO: clear defunct chats
                    
                    # update chats
                    for chat_name in self.chat_handlers:
                        chat_handler = self.chat_handlers[ chat_name ]
                        new_messages = chat_handler.update()
                        if len(new_messages)> 0:
                            print "New messages in chat: %s" % chat_handler.chat.FriendlyName
                        for new_message in new_messages:
                            body = new_message.Body
                            print body
                            try:
                                for commandstring in command_mappings:
                                    commandbang = "!" + commandstring
                                    bl = body.lower()
                                    command = command_mappings[ commandstring ]
                                    message_out = None
                                    
                                    # if command is giftable
                                    if hasattr( command, 'gift' ):
                                        giftstring = "%s for " % commandbang
                                        if giftstring in bl:
                                            print "Gift command %s" % commandbang
                                            loc = body.find(giftstring) + len(giftstring)
                                            spc = body.find( " ", loc )
                                            recicpient = body[ loc : spc ]
                                            print "-> finding recipient '%s'" % recicpient
                                            members = chat_handler.chat.Members
                                            print members
                                            for member in members:
                                                print "member: %s" % member
                                                dn = member.DisplayName
                                                print dn
                                                if recicpient.lower() in dn.lower():
                                                    print "-->  gift %s to %s " % (commandbang, recicpient)
                                                    message_out = command.gift( dn )
                                                    break

                                    if message_out is None and commandbang in bl:
                                        message_out = command.execute( new_message )

                                    if message_out is not None:
                                        chat_handler.chat.SendMessage( message_out )
                                        tw.tweet( message_out )

                            except Exception, e:
                                logging.info( e )
                                print e
                    time.sleep(1)
            except Exception, e:
                logging.info( e )
                print e