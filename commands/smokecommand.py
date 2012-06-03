# coding=UTF-8

from string import Template
import random

class SmokeCommand(object):

	def __init__(self):

		self.templates = [ 	Template("hapily slides $name $smoke."),
							Template("produces a $smoke for $name and asks if a light is required"),
							Template("flips his Zippo and slides it along the bar to $name"),
							Template("slides a fresh ashtray down the bar, followed by $smoke"),
							Template("coughs and passes $name $smoke"),
							Template("suggests a !snack might be heathier"),
							Template("walks into the humador and brings out $smoke"),
							Template("reaches under the counter and brings out $smoke"),
							Template("reaches over to $name and lights up a $smoke"),
							Template("eyeballs $name for a moment, then gingerly hands $smoke across the bar.") ]

		self.pre_modifiers = [ "an ancient",
				   "a smooth",
				   "a dry old",
				   "a fresh",
				   "a glitchy",
				   "a smoldering",
				   "an exquisite",
				   "a hand rolled",
				   "a cheap"]				

		self.smokes = [ "pack of Marlboros (smoking)",
			"Tesco value cigar",
			"pipe full of herbal voodoo",
			"bong packed with oddly smelling green tabacco",
			"Rothschild",
			"Robusto",
			"Robusto",
			"a Petit Corona",
			"Carlota",
			"Corona",
			"Corona Gorda",
			"Panatela",
			"Toro",
			"Corona Grande",
			"Lonsdale",
			"Churchill",
			"Double Corona",
			"Presidente",
			"Gran Corona",
			"Double Toro",
			"Gordo",
			"Hookah with Apple tobacco to share with everyone"]

	def execute( self, message ):
		smoke = random.choice( self.smokes )
		pre_modifier = random.choice( self.pre_modifiers )
		smoke = "%s %s" % (pre_modifier, smoke)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, smoke=smoke)
		return "/me %s" % message_out

