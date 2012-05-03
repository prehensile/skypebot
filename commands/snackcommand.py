from string import Template
import random

class SnackCommand(object):

	def __init__(self):

		self.templates = [ 	Template("begrudgingly serves $name $snack."),
							Template("ostentatiously prepares $name $snack and pockets the change."),
							Template("eyeballs $name for a moment, then shoves $snack across the bar."),
														]

		self.pre_modifiers = [ "a perfect",
				   "a stingy",
				   "an old",
				   "a fresh",
				   "a glitchy",
				   "a cheap" ]				

		self.drinks = [ "Bacon Roll",
			"Packet of Crisps",
			"Bag of Nuts",
			"Mars Bar",
			"Snickers",
			"Marathan",
			"Milky Way",
			"Sausage Cob with Brown Sauce",
			"Pretzel",
			"Bowl of Wasabi Nuts ]

	def execute( self, message ):
		drink = random.choice( self.drinks )
		pre_modifier = random.choice( self.pre_modifiers )
		if(pre_modifier[-1].lower() == 'a') and (drink[:1].lower()=='a'):
			pre_modifier += "n"
		drink = "%s %s" % (pre_modifier, drink)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, drink=drink)
		return "/me %s" % message_out

