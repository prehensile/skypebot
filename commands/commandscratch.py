# coding=UTF-8
from string import Template
import random
import commandbase

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
class ExampleCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("lobs a dolphin at $name.") ]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
		

class KnockKnockCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("asks who's there.") ]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
		
class BashfordCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("is algoraving."),
					Template("shares a genrememe track."),
					Template("is commuting to Hamburg."),
					Template("is buying a hugely overpriced jacket for Arctic Marathon Swimmers."),
					Template("is listening to EMF"),
					Template("is searching YouTube for YetiCore videos."),
					Template("is eating a steak."),
					Template("is sharing the wrong YouTube track."),
					Template("seapunked all over the shop."),
					Template("seapunked all over the shop."),
					Template("is a Thing now."),]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out