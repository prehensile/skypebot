# coding=UTF-8
from string import Template
import random

class MarcusCommand(object):

	def __init__(self):
		self.templates = [ 	Template("tells a story."),
							Template("makes it transmedia."),
							Template("ponders the tinyweb."),
							Template("gets a larger pair of glasses"),
							Template("puts on a wig."),
							Template("giggles."),
							Template("engages Big Hand Mode."),
							Template("is really telling you something here. #globe_hands"),
							Template("paints his face white."),
							Template("stalks $name."),
							Template("broadcasts from the toliet."),
							Template("sells $name some used web.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out