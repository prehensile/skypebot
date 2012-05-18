from string import Template
import random

class BirthdayCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("strings up the bunting and launches a party popper into $name's drink"),
		 					Template("lights up some everlasting candles and shoves them into a pile of !snack"),
		 					Template("sombrely reminds all present that each birthday is a year closer to death before tweaking $name's nose and runnning off cackling into the cellar.") ]
	
	def generate( self, recipient ):
		template = random.choice( self.templates )
		message_out = template.substitute( name=recipient )
		return "/me %s" % message_out

	def execute( self, message ):
		name = message.FromDisplayName
		return self.generate( name )

	def gift( self, recipient ):
		return self.generate( name )