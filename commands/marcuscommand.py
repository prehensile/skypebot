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
							Template("is enjoying the benefits of an excellent hangover."),
							Template("is dating Pambot."),
							Template("thinks Marcus has got a little bit carried away using his ego-command."),
							Template("giggles."),
							Template("engages Big Hand Mode."),
							Template("is really telling you something here. #globe_hands"),
							Template("paints his face white."),
							Template("stalks $name."),
							Template("broadcasts from the toliet."),
							Template("retires a version of himself"),
							Template("smacks a unicorn"),
							Template("flies off on a tangent"),
							Template("considers the drillability of it all"),
							Template("uses a nasty hashtag"),
							Template("makes a spelling mistake"),
							Template("says something in German"),
							Template("clones himself"),
							Template("forgets to commit the changes"),
							Template("eats some sausage"),
							Template("books a table at the Schwarzer Hahn"),
							Template("takes a photograph of !satan"),
							Template("sells $name some used web.")
							]
							
	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out