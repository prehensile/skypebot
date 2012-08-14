import logging
import Skype4Py
import datetime
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
                #print message.Id
        return new_messages

class SkypeConnector(object):
    
    def __init__( self, attach=True ):
        self.skype = Skype4Py.Skype(Transport='x11')
        self.chat_handlers = {}
        if( attach ):
            logging.info( "Attaching to Skype..." )
            self.skype.Attach()

    def message_all( self, message ):
        lines = message.split("\n")
        # send message to all connected chats   
        for chat_name in self.chat_handlers:
            chat_handler = self.chat_handlers[ chat_name ]
            try:
                for line in lines:
                    chat_handler.chat.SendMessage( message )
            except Exception, e:
                logging.info( e )

    def update_chats( self ):

        # maintain list of chats
        chats = self.skype.ActiveChats
        defunct_chat_names = set( self.chat_handlers.keys() )
        for chat in chats:
            chat_name = chat.Name
            try: 
                defunct_chat_names.remove( chat_name )
            except KeyError:
                pass
            if chat_name not in self.chat_handlers:
                logging.info( "New handler for chat: %s" % chat.FriendlyName )
                self.chat_handlers[chat_name] = ChatHandler(chat)
                message = housekeeping.new_chat_message()
                try:
                    chat.SendMessage( message )
                except Exception, e:
                    logging.info( e )
                    print e

        # clear defunct chats
        for defunct_chat_name in defunct_chat_names:
            logging.info( "Delete handler for chat: %s" % defunct_chat_name )
            del self.chat_handlers[ defunct_chat_name ]
        
        return self.chat_handlers        