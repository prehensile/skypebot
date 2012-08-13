# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class HaiCommand( BaseCommand ):

	def __init__(self):
		BaseCommand.__init__( self )
		self.command_mappings = [ "aces" ]
		self.templates = [ 	Template("tuts and nods at $name"),
							Template("points out to $name that 5 aces is suspect ."),
							Template("passes $name a !drink"),
							Template("marks it up on the board. deux points for $name")
							]
							
	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out