# coding=UTF-8

from string import Template
import random

class CockCommand(object):

	def __init__(self):

		self.templates = [ 	Template("magnificently glitches $name $drink all over Gregory Povey who now looks peeved. #time #cock"),
							Template("admirably reminds $name that Jon Ronson has passed away and tips $drink over Marcus Brown's head. #time #cock"),
							Template("tickles $name under the chin before making a rude joke about David Bausola. He then gives everyone in the bar $drink. #time #cock"),
							Template("weeps."),
							]

		self.pre_modifiers = [ "half a",
				   "a wet",
				   "a sad",
				   "a happy",
				   "a horrid",
				   "the new aesthetic version of a" ]				

		self.drinks = [ "Jon_Ronson",
			"Jon R0n50n",
			"j0n r0n5on",
			"nothing" ]

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
