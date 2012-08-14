# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class HaiCommand( BaseCommand ):

	def __init__(self):
		BaseCommand.__init__( self )
		self.command_mappings = [ "aces" ]
		self.templates = [ 	Template("tuts and nods at $name"),
							Template("points out to $name that 5 aces is suspect."),
							Template("passes $name a !drink."),
							Template("calls $name a !cock."),
							Template("throws a dolphin at $name."),
							Template("!ponders and calls $name's bluff with a full house."),
							Template("calls !bullshit on $name and dishes out the !cheese."),
							Template("grins and performs some tiny !magic for $name."),
							Template("chokes."),
							Template("disagrees."),
							Template("reopens the bubbly wine."),
							Template("looks concerned."),
							Template("instagrams the moment."),
							Template("shares the moment on Path."),
							Template("writes another rule in the tiny web manifesto."),
							Template("adds scampi to the dinner menu."),
							Template("marks it up on the board. deux points for $name.")
							]
							
	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out