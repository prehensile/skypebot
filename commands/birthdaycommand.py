# coding=UTF-8

from string import Template
import random
import commandbase

class BirthdayCommand( commandbase.BaseCommand ):

    def __init__(self):
        
        BaseCommand.__init__( self )

        self.command_mappings = [ "birthday" ]

        self.templates = [  Template("strings up the bunting and launches a party popper into $name's drink"),
                            Template("lights up some everlasting candles and shoves them into a pile of !snack"),
                            Template("sombrely reminds all present that each birthday is a year closer to death before tweaking $name's nose and runnning off cackling into the cellar.") ]
    
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute( name=name )
        return "/me %s" % message_out