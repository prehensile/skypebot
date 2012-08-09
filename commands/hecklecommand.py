# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class HeckleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("liked this better when no-one had heard of it."),
                            Template("thinks $name has totally sold out."),
                            Template("thinks $name is talking a load of post-whatsit !bullshit."),
                            Template("doesn't think much of $name's !handwork") ]
        self.command_mappings = [ "heckle" ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
