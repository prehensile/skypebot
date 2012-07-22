# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class CoffeeCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "Copperfield", "McGee", "maagik", "magikk" ]

        self.templates = [  Template("pulls out $thing from $name's $location and $finish."),
                            ]
        
        self.things = [ "a rabbit",
                    "a teapot",
                    "a donkey",
                    "a small bus",
                    "a dead dove",
                    "a glitchy sherry",
                    "$name's passport",
                    "a photo of !marcus from last Friday",
                    "Greg's wallet",
                    "a €20 coin",
                    "the DVD box set of Twin Peaks",
                    "a speedboat",
                    "a copy of Vogue July 1967",
                    "the Brass Band of Chicago",
                    "South Africa",
                    "a cold bag of chips",
                    "a massive currywurst",
                    "a pair of Snow Lepoards",
                    "the Olympic Torch",
                    "a BMX",
                    "a Solero",
                    "a TARDIS",
                    "David Copperfield",
                    "David Copperfield's mother",
                    "David Copperfield's private photo collection"]              

        self.locations = [ "left ear",
                    "right ear",
                    ]

        self.finishes = ["and gets his coat.",
                    "and takes a bow.",
                    "and winks at Pambot.",
                    "and winks at David.",
                    "and leaves.",
                    "and vanishes in a puff of smoke.",
                    "and leaves through the trapdoor.",
                    "and evaporates.",
                    "and teleports to Swindon.",
                    "and claps the tune of Blankety Blank.",
                    "and pedals off on the tiny tricycle.",
                    "and sniffs.",
                    "and asks for honest feedback.",
                    "and mumbles something about Debbie McGee in '89.",
                    "and pours himself a !drink",
                    "and !ponders."]







        
    def generate( self, name ):

        thing = random.choice( self.things )
        location = random.choice( self.locations )
        finish = random.choice( self.finishes )
        template = random.choice( self.templates )
        pre_modifier = random.choice( self.pre_modifiers )
        template = random.choice( self.templates )
        message_out = template.substitute(  name=name, 
                                            thing=thing,
                                            location=location,
                                            finish=finish)

        return "/me %s" % message_out











