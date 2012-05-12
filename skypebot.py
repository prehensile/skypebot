import Skype4Py
import time
from commands import drinkcommand, wetcommand, baconcommand, snackcommand, \
cheesecommand, cockcommand, smokecommand, chooncommand, tvcommand
import datetime
import json
import Queue
from hookserver import HookServerMessage, HookServerThread
import sys
import logging

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
class BotRunner( object ):
	
	def message_all( self, message ):
	# send message to all connected chats	
		for chat_name in self.chat_handlers:
			chat_handler = self.chat_handlers[ chat_name ]
			try:
				chat_handler.chat.SendMessage( message )
			except Exception, e:
				logging.info( e )

	def run( self ):

		return_code = 0

		# set up http server to listen for github pushes
		queue = Queue.Queue()
		hook_server = HookServerThread()
		hook_server.queue = queue
		hook_server.start()

		self.chat_handlers = {}
		command_mappings = {}
		command_mappings[ "drink" ] = drinkcommand.DrinkCommand()
		command_mappings[ "w3t" ] = wetcommand.WetCommand()
		command_mappings[ "bacon" ] = baconcommand.BaconCommand()
		command_mappings[ "snack" ] = snackcommand.SnackCommand()
		command_mappings[ "cheese" ] = cheesecommand.CheeseCommand()
		command_mappings[ "cock" ] = cockcommand.CockCommand()
		command_mappings[ "choon" ] = chooncommand.ChoonCommand()
		command_mappings[ "smoke" ] = smokecommand.SmokeCommand()
		command_mappings[ "tv" ] = tvcommand.TVCommand()

		if RUN_SKYPE:
			skype = Skype4Py.Skype(Transport='x11')
			skype.Attach()
		
		_run = True
		first_run = True
		while _run:
			try:
				if RUN_SKYPE:
					# maintain list of chats
					chats = skype.Chats
					for chat in chats:
						chat_name = chat.Name
						if chat_name not in self.chat_handlers:
							print "New handler for chat: %s" % chat.FriendlyName
							self.chat_handlers[chat_name] = ChatHandler(chat)
							if first_run is True:
								chat.SendMessage("/me appears a split nanosecond after his ratty carpet slippers do.")
					# TODO: clear defunct chats
					
					first_run = False

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
									if "!" + commandstring in body.lower():
										command = command_mappings[ commandstring ]
										message_out = command.execute( new_message )
										if message_out is not None:
											chat_handler.chat.SendMessage( message_out )
							except Exception, e:
								logging.info( e )
								print e
				
				# check for updates from the HTTP server thread
				hook_message = None
				try:
					hook_message = queue.get( False )
				except Queue.Empty:
					pass

				if hook_message is not None:
					if hook_message.code == HookServerMessage.RECIEVED_PUSH:
						commits = hook_message.payload[ 'commits' ]
						commit_author = commits[0]['author']['name']
						message_out = "/me goes glassy eyed for a moment as an update is recieved. If he doesn't come back it's %s's fault." % commit_author
						self.message_all( message_out )
						_run = False
						return_code = 3
				else: 
					time.sleep( 1 )

			except KeyboardInterrupt:
				_run = False

			if _run is False:
				# for chat_name in self.chat_handlers:
				# 	chat_handler = self.chat_handlers[ chat_name ]
				# 	try:
				# 		chat_handler.chat.Leave()
				# 	except Exception, e:
				# 		logging.info( e )
				break

		hook_server.stop()
		return return_code
	

runner = BotRunner()
retcode = runner.run()
sys.exit( retcode )

