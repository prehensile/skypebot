# coding=UTF-8

from string import Template
import random

class TeaCommand(object):

	def __init__(self):

		self.templates = [ 	Template("pours $name $snack."),
							Template("stares glassy eyed at $name, then slides $snack across the bar."),
							Template("looks longingly at the optics, sighs and hands $name $snack")]

		self.pre_modifiers = [ "a massive mug of",
				   "some stewed",
				   "a fine blend of",
				   "a freshly brewed" ]				

		self.snacks = [ "Assam",
			"Darjeeling First Flush",
			"Builders",
			"Earl Grey",
			"single estate Ceylon",
			"100 year old handrolled Oolong",
			"Lapsang Souchong",]

	def execute( self, message ):
		snack = random.choice( self.snacks )
		pre_modifier = random.choice( self.pre_modifiers )
		snack = "%s %s" % (pre_modifier, snack)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, snack=snack)
		return "/me %s" % message_out

