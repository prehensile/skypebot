# coding=UTF-8

from string import Template
import random

class RumbleCommand(object):

	def __init__(self):

		self.templates = [ 	Template("pounces $name with a $finisher."),
							Template("performs a $finisher on $name and watches as they tap out."),
							Template("tries a $finisher on $name before realising $name really just needs a hug.")
						 ]

		self.pre_modifiers = [ "sloppy",
				   "aggressive",
				   "half-assed attempt of a",
				   "too weak to matter"
				   ]				

		self.finishers = [ "Devils Gate",
			"Emerald City Twister",
			"Axe Bomber",
			"Hulk-Buster",
			"Russian Sickle",
			"Mandible Claw",
			"Steele Trap"]

	def execute( self, message ):
		finisher = random.choice( self.finishers )
		pre_modifier = random.choice( self.pre_modifiers )
		finisher = "%s %s" % (pre_modifier, finisher)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, finisher=finisher)
		return "/me %s" % message_out

