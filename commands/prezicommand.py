# coding=UTF-8
from string import Template
import random
import commandbase

class PreziCommand( commandbase.BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "prezi" ]
        self.templates = [  Template("zooms in on a hoover."),
                            Template("zooms in on $name.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class FractalCommand( commandbase.BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "fractal" ]
        self.templates = [  Template("zooms in on The Landlord.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
        

        