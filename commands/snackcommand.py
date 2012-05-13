from string import Template
import random

class SnackCommand(object):

	def __init__(self):

		self.templates = [ 	Template("begrudgingly serves $name $snack."),
							Template("ostentatiously prepares $name $snack and pockets the change."),
							Template("surprises everyone again with (cake)"),
							Template("eyeballs $name for a moment, then shoves $snack across the bar.") ]

		self.pre_modifiers = [ "a perfect",
				   "a stingy",
				   "an old",
				   "a fresh",
				   "a glitchy",
				   "a cheap" ]				

		self.snacks = [ "Bacon Roll",
			"packet of Crisps",
			"bag of Nuts",
			"Mars Bar",
			"Snickers",
			"Marathan",
			"Milky Way",
			"Sausage Cob with Brown Sauce",
			"Pretzel",
			"packet of Scampi Fries",
			"Bowl of Wasabi Nuts",
			"Curly Wurly"]

	def execute( self, message ):
		snack = random.choice( self.snacks )
		pre_modifier = random.choice( self.pre_modifiers )
		snack = "%s %s" % (pre_modifier, snack)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, snack=snack)
		return "/me %s" % message_out

