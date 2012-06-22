# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class RumbleCommand( BaseCommand ):

	def __init__(self):

		BaseCommand.__init__( self )
		
		self.command_mappings = [ "brawl", "rumble" ]

		self.templates = [ 	Template("pounces $name with a $finisher."),
							Template("performs a $finisher on $name and watches as they tap out."),
							Template("wears a flashy dressing grown and shouts 'WOOOOOOO'."),
							Template("is suspended for 30-days due to a violation of the Wellness Program."),
							Template("botches a $finisher and $name is stretchered out of the ring."),
							Template("hollers at Miss Elizabeth."),
							Template("turns heel."),
							Template("calls $name's momma."),
							Template("cuts a promo and fluffs his lines."),
							Template("tears his vest."),
							Template("pops."),
							Template("interrupts $name by shouting 'what'."),
							Template("joins $name's stable."),
							Template("squashes $name."),
							Template("is suffering from ring rust."),
							Template("is getting a heavy push."),
							Template("500lbs, 6 foot 7, from Parts Unknown."),
							Template("thinks $name is a paper champion."),
							Template("laughs as low-carder $name challenges him."),
							Template("has legit heat with $name."),
							Template("juices."),
							Template("goes to the top-rope."),
							Template("introduces a foreign object into the !rumble."),
							Template("hazes $name."),
							Template("feuds with $name."),
							Template("sandbags $name."),
							Template("is disgusted by the Philter Bar Screw Job."),
							Template("gets a cheap pop by delivering a $finisher on $name."),
							Template("gets buried by Creative."),
							Template("does a bit of blading."),
							Template("tags $name into the ring."),
							Template("calls out Chris Brown."),
							Template("tweets to @marcusjhbrown. #kayfabe."),
							Template("goes over $name."),
							Template("works a dark match with $name.."),
							Template("is drafted to Smackdown."),
							Template("jobs to $name on Superstars."),
							Template("forms a tag-team with $name."),
							Template("can smell what $name is cooking."),
							Template("has a hashtag on his trunks."),
							Template("puts $name in a coffin."),
							Template("catches $name off guard with a low-blow."),
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

	def generate( self, name ):
		finisher = random.choice( self.finishers )
		pre_modifier = random.choice( self.pre_modifiers )
		finisher = "%s %s" % (pre_modifier, finisher)
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, finisher=finisher)
		return "/me %s" % message_out

