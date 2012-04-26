import Skype4Py
import time
import commands
import datetime

class ChatHandler(object):
	
	def __init__( self, Chat ):
		self.chat = Chat
		self.last_timestamp = datetime.datetime.now()

	def update( self ):
		ts = datetime.datetime.now()
		new_messages = []
		messages = self.chat.RecentMessages
		for message in messages:
			dt = message.Datetime
			if dt > self.last_timestamp:
				new_messages.append( message )
				self.last_timestamp = dt
		return new_messages

def main():

	skype = Skype4Py.Skype(Transport='x11')
	skype.Attach()

	chat_handlers = {}

	command_mappings = {}
	command_mappings[ "drink" ] = commands.DrinkCommand()

	while 1:
		# maintain list of chats
		chats = skype.Chats
		for chat in chats:
			chat_name = chat.Name
			if chat_name not in chat_handlers:
				print "New handler for chat: %s" % chat.FriendlyName
				chat_handlers[chat_name] = ChatHandler(chat)
		# TODO: clear defunct chats
		
		# update chats
		for chat_name in chat_handlers:
			chat_handler = chat_handlers[ chat_name ]
			new_messages = chat_handler.update()
			if len(new_messages)> 0:
				print "New messages in chat: %s" % chat_handler.chat.FriendlyName
			for message in new_messages:
				body = message.Body
				print body
				for commandstring in command_mappings:
					if "!" + commandstring in body.lower():
						command = command_mappings[ commandstring ]
						message_out = command.execute( message )
						if message_out is not None:
							chat_handler.chat.SendMessage( message_out )
					
		time.sleep( 1 )

main()
