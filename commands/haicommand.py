# coding=UTF-8

from string import Template
import random

class HaiCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("hides behind the bar as $name enters."),
							Template("runs away, screaming 'not again!' as he remembers $name from his ancient personal history"),
							Template("is bemused as $name seems to think their kind get served in here."),
							Template("welcomes $name, and opens the hidden door to the gambling room."),
							Template("forcibly ejects another patron as they sit in $name's usual spot."),
							Template("calls the law. This $name character looks like he’s up to no good.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out