# coding=UTF-8

from string import Template
import random

class RumbleCommand(object):

	def __init__(self):

		self.templates = [ 	Template("pounces $name with a $finisher."),
							Template("performs a $finisher on $name and watches as they tap out."),
							Template("sets up a $finisher on $name and screams YES YES YES."),
							Template("tries a $finisher on $name before realising $name really just needs a hug.")
						 ]

		self.pre_modifiers = [ "sloppy",
				   "aggressive",
				   "half-assed attempt of a",
				   "pathetic",
				   "must see",
				   "PPV",
				   "girly",
				   "delicate",
				   "impressive but inaffective",
				   "smashing",
				   "crushing",
				   "horrible",
				   "buggered up",
				   "too weak to matter"
				   ]				

		self.finishers = [ "Devils Gate",
			"Emerald City Twister",
			"Axe Bomber",
			"Hulk-Buster",
			"Russian Sickle",
			"Mandible Claw",
			"Big Splash",
			"Boday Avalanche",
			"Bronco Buster",
			"Backhand Chop",
			"Flying Clothesline",
			"Butt Drop",
			"Elbow Drop",
			"Headbut",
			"Discus Elbow Smash",
			"Povey Ponce Breaker",
			"Bausola Bowel Slam",
			"Shardcore Elbow Bounce",
			"Go To Sleep"
			"Kaiser Wobble Bash",
			"Snake Eyes",
			"Mjays Eye Poke",
			"Steele Trap"]

	def execute( self, message ):
		finisher = random.choice( self.finishers )
		pre_modifier = random.choice( self.pre_modifiers )
		finisher = "%s %s" % (pre_modifier, finisher)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, finisher=finisher)
		return "/me %s" % message_out

