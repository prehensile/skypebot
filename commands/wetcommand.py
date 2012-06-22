# coding=UTF-8

from string import Template
import random
import commandbase

class WetCommand( commandbase.BaseCommand ):

    def __init__(self):
        self.command_mappings = [ "w3t", "splashy" ]
        self.templates = [  Template("lobs a dolphin at $name.") ]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
