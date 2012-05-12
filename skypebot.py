import Skype4Py
import time
from commands import drinkcommand, wetcommand, baconcommand, snackcommand, \
cheesecommand, cockcommand
import datetime
import json
import Queue
from hookserver import HookServerMessage, HookServerThread
import sys

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

RUN_SKYPE=False
class BotRunner( object ):
	
	def run( self ):

		return_code = 0

		# set up http server to listen for github pushes
		queue = Queue.Queue()
		hook_server = HookServerThread()
		hook_server.queue = queue
		hook_server.start()

		chat_handlers = {}
		command_mappings = {}
		command_mappings[ "drink" ] = drinkcommand.DrinkCommand()
		command_mappings[ "w3t" ] = wetcommand.WetCommand()
		command_mappings[ "bacon" ] = baconcommand.BaconCommand()
		command_mappings[ "snack" ] = snackcommand.SnackCommand()
		command_mappings[ "cheese" ] = cheesecommand.CheeseCommand()
		command_mappings[ "cock" ] = cockcommand.CockCommand()
		command_mappings[ "choon" ] = chooncommand.ChoonCommand()
		command_mappings[ "smoke" ] = chooncommand.SmokeCommand()
		command_mappings[ "tv" ] = tvcommand.TVCommand()

		if RUN_SKYPE:
			skype = Skype4Py.Skype(Transport='x11')
			skype.Attach()
		try:
			_run = True
			while _run:
				if RUN_SKYPE:
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
				
				# check for updates from the HTTP server thread
				message = None
				try:
					message = queue.get( False )
				except Queue.Empty:
					pass

				if message is not None:
					if message.code == HookServerMessage.RECIEVED_PUSH:
						commits = message.payload[ 'commits' ]
						commit_author = commits[0]['author']['name']
						message_out = "/me goes glassy eyed for a moment as an update is recieved. If he doesn't come back it's %s's fault." % commit_author
						_run = False
						return_code = 3

				if _run:
					time.sleep( 1 )
		
		except KeyboardInterrupt:
			pass

		hook_server.stop()
	

runner = BotRunner()
retcode = runner.run()
sys.exit( retcode )

