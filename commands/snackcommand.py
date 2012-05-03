from string import Template
import random

class SnackCommand(object):

	def __init__(self):

		self.templates = [ 	Template("begrudgingly serves $name $snack."),
							Template("ostentatiously prepares $name $snack and pockets the change."),
							Template("eyeballs $name for a moment, then shoves $snack across the bar."),
														]

		self.pre_modifiers = [ "a big bag of",
				   "a stingy",
				   "old",
				   "fresh",
				   "a glitchy",
				   "cheap" ]				

		self.drinks = [ "Bacon Roll",
			"Crisps",
			"Nuts",
			"Pretzels",
			"Wasabi Nuts ]

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

