# coding=UTF-8
from string import Template
import random

class PoveyCommand(object):

	def __init__(self):
		self.templates = [ 	Template("thinks $name completes him."),
							Template("nurtures a hangover.")
							Template("buggers up a branch.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out