# coding=UTF-8

from string import Template
import random

class TeaCommand(object):

	def __init__(self):

		self.templates = [ 	Template("pours $name $tea."),
							Template("stares glassy eyed at $name, then slides $tea across the bar."),
							Template("looks longingly at the optics, sighs and hands $name $tea")]

		self.pre_modifiers = [ "a massive mug of",
				   "some stewed",
				   "a fine blend of",
				   "a freshly brewed" ]				

		self.teas = [ "Assam",
			"Darjeeling First Flush",
			"Builders",
			"Earl Grey",
			"single estate Ceylon",
			"100 year old handrolled Oolong",
			"Lapsang Souchong"]

	def execute( self, message ):
		tea = random.choice( self.teas )
		pre_modifier = random.choice( self.pre_modifiers )
		tea = "%s %s" % (pre_modifier, tea)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, tea=tea)
		return "/me %s" % message_out

