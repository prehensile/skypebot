# coding=UTF-8
from string import Template
import random

class PoveyCommand(object):

	def __init__(self):
		self.templates = [ 	Template("thinks $name completes him."),
							Template("nurtures a hangover."),
							Template("organises a conference"),
							Template("makes some badges"),
							Template("puts Side B on."),
							Template("corrects !marcus' spelling."),
							Template("instagrams the cat."),
							Template("automagically grows a beard"),
							Template("buggers off to Denmark for a bit."),
							Template("nips out the back to catch up with the wrestling"),
							Template("was on the best seat in the bus this morning"),
							Template("calls $name a divvy"),
							Template("buggers up a branch.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out