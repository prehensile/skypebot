# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class VoodooCommand( BaseCommand ):

	def __init__(self):
	
		BaseCommand.__init__( self )
		
		self.command_mappings = [ "voodoo", "witch", "spell", "magic", "trick" ]
		
			self.templates = [ 	Template("plucks out a couple of $name's hairs and runs off."),
						Template("explains voodoo economics to $name. $name still doesn't get it." ),
						Template("shows off his voodoo globe. He spins it real fast and everybody freaks out.”"),
						Template("serves his specialty voodoo donut to $name, who takes a bite. somewhere, millions scream out in pain."),
						Template("cuts the head off a bot and chucks it at $name."),
						Template("is pinstruck."),
						Template("mutters an incantation in $name's general direction."),
						Template("shakes a rattle and dances in a circle around $name."),
						Template("explains to $name that Hollywood has ruined voodoo's reputation. Chucks a chicken head at the tv."),
						Template("sticks a pin in a bot with the likeness of $name. $name falls over in pain."),
						Template("casts a love spell on $name, who promptly falls head over heels for a Weavr"),
						Template("sells $name a shrunken bot head, which vaguely resembles !povey.."),
						Template("holds $name's bot over a candle. something smells of !bacon.")
							]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out