# coding=UTF-8
from string import Template
import random

class BaconCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("begrudgingly serves $name $bacon."),
							Template("wangs a load of $bacon on the grill for $name."),
							Template("trims the fat off some $bacon for $name."),
							Template("brushes the fur off the $bacon for $name."),
							Template("lovingly strokes $bacon before sexily laying it across the hot, naughty pan for $name.") ]
		
		self.bacon = [ "smokey bacon",
			"back bacon",
			u'Stegt Flæsk',
			"Slavink",
			"Szalonna",
			"Salt pork",
			"Samgyeopsal",
			"pigs in blanket",
			"pig candy",
			"Mitch Morgan",
			"Kranjska klobasa",
			"Jambonette",
			"Hangtown fry",
			"Guanciale",
			"Fool's Gold Loaf",
			u'Čvarci',
			"Chocolate covered bacon",
			"Chicken fried bacon",
			"BLT sandwich",
			"Bacone",
			"Bacon ice cream",
			"Bacon explosion",
			"Bacon bits",
			"Bacon and egg pie",
			"Bacon and cabbage",
			"Angels on horseback",
			u'Æbleflæsk',
			"streaky bacon",
			"smoked back bacon",
			"dry cured bacon",
			"honey cured bacon",
			"hand-reared" ]

	def execute( self, message ):
		bacon = random.choice( self.bacon )
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, bacon=bacon)
		return "/me %s" % message_out
