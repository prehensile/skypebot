# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ShardcoreCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "shardcore" ]
        self.templates = [  Template("paints a lovely painting of Morrissey."),
                            Template("is told to bite his tongue by $name."),
                            Template("is denied access to the United States of Botstep."),
                            Template("is disappointed by all the swearing."),
                            Template("just wants to finger paint."),
                            Template("sacks his cleaner."),
                            Template("misses the real world."),
                            Template("doesn't have a face."),
                            Template("draws a face on his cock-tip."),
                            Template("has declared world domination of techno sleaze has is ultimate goal."),
                            Template("has a serious chat with the cleaning lady.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out