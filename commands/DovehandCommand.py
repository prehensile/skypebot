# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DovehandCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "dovehand", "hands" ]

          self.templates = [  Template("performs $hand."),
                              Template("shows off $hand.")
                           ]
        
          self.pre_modifiers = [ "sloppy",
                                 "uninspired",
                                 "surprising",
                                 "enormous",
                                 "papier-mache",
                                 "textbook",
                                 "glitchy",
                                 "withering",
                                 "tingly",
                                 "uninspired"
                               ]                
        
          self.hands = [ "dovehands",
                         "rubber hands",
                         "globe hands",
                         "melon weighing",
                         "shelf stacking",
                         "big fish little fish",
                         "tiny hands",
                         "futureclaw",
                       ]

    def generate( self, name ):
        hand = random.choice( self.hands )
        pre_modifier = random.choice( self.pre_modifiers )
        if(pre_modifier[-1].lower() == 'a') and (hand[:1].lower()=='a'):
            pre_modifier += "n"
        hand = "%s %s" % (pre_modifier, hand)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, hand=hand)
        return "/me %s" % message_out
        