# coding=UTF-8

from string import Template
import random
import commandbase

class HaiCommand( commandbase.BaseCommand ):

	def __init__(self):
		BaseCommand.__init__( self )
		self.command_mappings = [ "hai", "ohai", "hallo", "morning", "afternoon", "evenin" ]
		self.templates = [ 	Template("hides behind the bar as $name enters."), #OK
							Template("runs away, screaming 'not again!'. He remembers $name from his ancient personal history."),
							Template("is bemused as $name seems to think their kind get served in here."), #OK
							Template("smashes a beer bottle, tells $name they're not welcome round here."), #OK
							Template("gives $name a devastatingly warm bearhug. Lingers a little too long."), #OK
							Template("cracks open the sparkling wine to celebrate $name arriving."),
							Template("rues the day he let $name become a member."), #OK
							Template("welcomes $name, and opens the hidden door to the gambling room."), #OK
							Template("forcibly ejects another patron as they sit in $name's usual spot."),
							Template("calls the law. This $name character looks like they're up to no good."),
							Template("looks up as $name enters, checks their name off his Special List")
							]
							
	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out