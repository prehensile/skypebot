import Skype4Py
import time
import commands

class ChatHandler(object):
	
	def __init__( self, Chat ):
		self.chat = Chat
		self.last_timestamp = None

	def update( self ):
		new_messages = []
		messages = self.chat.RecentMessages
		for message in messages:
			dt = message.Datetime
			if (self.last_timestamp is None) or (dt>self.last_timestamp):
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
				chat_handlers[chat_name] = ChatHandler(chat)
		# TODO: clear defunct chats
		
		# update chats
		for chat_name in chat_handlers:
			chat_handler = chat_handlers[ chat_name ]
			new_messages = chat_handler.update()
			for message in new_messages:
				body = message.Body
				if body.startswith("!"):
					idx = 0
					try:
						idx = body.index(" ")
					except ValueError,e:
						idx = len(body)
					commandstring = body[1:idx]
					if commandstring in command_mappings:
						command = command_mappings[ commandstring ]
						message_out = command.execute( message )
						if message_out is not None:
							chat_handler.chat.SendMessage( message_out )
					
		time.sleep( 1 )

main()
