# coding=UTF-8

from string import Template
import random

class RumbleCommand(object):

	def __init__(self):

		self.templates = [ 	Template("pounces $name with a $finisher."),
							Template("performs a $finisher on $name and watches as they tap out."),
							Template("wears a flashy dressing grown and shouts 'WOOOOOOO'."),
							Template("is suspended for 30-days due to a violation of the Wellness Program."),
							Template("botches a $finisher and $name is stretchered out of the ring."),
							Template("hollers at Miss Elizabeth."),
							Template("interferes as !marcus is trying to pin $name."),
							Template("smashes a steel-chair across $name's back."),
							Template("challenges $name to a Hell In The Philter Cell match."),
							Template("is entering the Royal Rumble at number 30."),
							Template("drops a pipebomb."),
							Template("takes a mouthful of water and sprays it all over $name."),
							Template("performs a worked shoot, calls out $name."),
							Template("takes the snake out of the bag."),
							Template("waves his Intercontinental Champion belt in $name's face. Oooooh yeeeeah."),
							Template("is wearing leather chaps."),
							Template("promotes the core values of Hustle, Loyalty, Respect"),
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
			"Go To Sleep",
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

