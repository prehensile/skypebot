# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class ElvisCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )

        self.command_mappings = [ "elvis" ]

        self.templates = [
            Template("announces that $honorific $rooming the building"),
            Template("$reaction as $honorific $action"),
            Template("$reaction as $honorific $action #$ejaculation"),
            Template("$ejaculation"),
            Template("observes that Elvis was a hero to most..."),
            Template("El-El-El-El-Elvis!"),
        ]         

        self.honorifics = [ "The King",
                            "The King of Rock and Roll",
                            "The Legend",
                            "The Leather-Clad Crooner",
                            "The White Suited Cabaret Act",
                            "The Bequiffed Artiste" ]
        
        self.roomings = [ "is entering",
                          "has entered",
                          "is in",
                          "is leaving",
                          "has left" ]

        self.actions = [ "hands out garishly hued silk scarves",
                         "croons",
                         "belts out a classic",
                         "wipes the sweat from his brow with a towel",
                         "shops the Beatles to J. Edgar Hoover",
                         "eats a second pizza",
                         "sings his heart out",
                         "grins back",
                         "scowls back",
                         "curls his lip",
                         "gyrates his hips" ]

        self.ejaculations = [ "uhuhuh",
                              "thankyouverymuch",
                              "uhthankyouverymuch" ]
        
        self.reactions = [ "weeps",
                           "watches transfixed",
                           "shakes his head",
                           "grins",
                           "wipes the bar",
                           "collects empties",
                           "looks lost in reflection",
                           "is overcome by melancholy",
                           "sneaks a crafty joint" ]

    def generate( self, name ):
        honorific = random.choice( self.honorifics )
        rooming = random.choice( self.roomings )
        ejaculation = random.choice( self.ejaculations )
        action = random.choice( self.actions )
        reaction = random.choice( self.reactions )
        template = random.choice( self.templates )
        message_out = template.substitute( name=name,
                                           honorific=honorific,
                                           rooming=rooming,
                                           ejaculation=ejaculation,
                                           action=action,
                                           reaction=reaction)
        return "/me %s" % message_out
