from string import Template
import random

class CoffeeCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("stares at $name, disregards the order and serves an home-roasted espresso ristretto.") ]
		
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
