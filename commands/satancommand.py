# coding=UTF-8
from string import Template
import random

class SatanCommand(object):

	def __init__(self):
		self.templates = [ 	Template("considers the infomorph aesthetic."),
							Template("draws a martini."),
							Template("thinks the bald mullet is an excellent look."),
							Template("wears a nice hat."),
							Template("rolls the 20-sided die for the RPG Wankmaster."),
							Template("exhales a thick fug."),
							Template("cooks up a nice batch of wasabi dumplings."),
							Template("shuffles to some botstep."),
							Template("commanded during Witching."),
							Template("is listening to the director's commentary on Blade Runner."),
							Template("is in Act 2, Stage IV: atonement with the father."),
							Template("rolls up.") ]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out

class MulletCommand(object):

	def __init__(self):
		self.templates = [ 	Template("shakes his head.") ]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out