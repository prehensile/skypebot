# coding=UTF-8

from string import Template
import random

class HaiCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("hides behind the bar as $name enters."),
							Template("runs away, screaming 'not again!' as he remembers $name from his ancient personal history")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out