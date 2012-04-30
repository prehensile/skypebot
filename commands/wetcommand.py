from string import Template
import random

class WetCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("lobs a dolphin at $name.") ]
		
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
