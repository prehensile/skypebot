# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DovehandCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "dovehand", "hand", "hands" ]

          self.templates = [  Template("performs $hand."),
                              Template("shows off $hand."),
                              Template("delivers $hand."),
                              Template("lingers over the !prezi with $hand.")
                           ]
        
          self.pre_modifiers = [ "a sloppy",
                                 "an uninspired",
                                 "a surprising",
                                 "an enormous",
                                 "a papier-mache",
                                 "a textbook",
                                 "a glitchy",
                                 "a withering",
                                 "a tingly",
                                 "a romantic",
                                 "an amateur",
                                 "a pro",
                                 "an intimate",
                                 "an unorthodox",
                                 "a distinguished",
                                 "a noble",
                                 "a justified",
                                 "a minced",
                                 "a relaxed",
                                 "an obtuse",
                                 "an erect",
                                 "an atrocious",
                                 "an endless",
                                 "a forgiving",
                                 ]                
        
          self.hands = [ "dovehands",
                         "rubber hands",
                         "globe hands",
                         "melon weighing",
                         "shelf stacking",
                         "big fish little fish",
                         "tiny hands",
                         "T-Rex",
                         "cupping",
                         "chop",
                         "pyramid",
                         "YMCA",
                         "winding of the gears",
                         "one-armed boxer",
                         "wave of change",
                         "chicken wing",
                         "layer cake",
                         "globe fist",
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
        