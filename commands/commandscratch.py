# coding=UTF-8
from string import Template
import random

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
class ExampleCommand(object):

	def __init__(self):
		self.templates = [ 	Template("lobs a dolphin at $name.") ]

	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out

## !satan command below here - GP

class SatanCommand(object):

	def __init__(self):
		self.templates = [ 	Template("considers the infomorph aesthetic."),
							Template("draws a martini."),
							Template("wears a nice hat."),
							Template("cooks up a nice batch of wasabi dumplings."),
							Template("shuffles to some botstep."),
							Template("rolls up.") ]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out