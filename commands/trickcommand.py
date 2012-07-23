# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class CoffeeCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "Copperfield", "McGee", "maagik", "magikk", "trick", "magic" ]

        self.templates = [  Template("$action $thing from $name\'s $location and $finish.")]
        

        self.actions = ["reveals",
                    "pulls out",
                    "teases out",
                    "produces"]


        self.things = [ "a rabbit",
                    "a teapot",
                    "a donkey",
                    "a small bus",
                    "a dead dove",
                    "a glitchy sherry",
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
                    "a pair of Snow Leopards",
                    "the Olympic Torch",
                    "a BMX",
                    "a Solero",
                    "a TARDIS",
                    "David Copperfield"]              

        self.locations = [ "left ear",
                    "right ear",
                    "left nostril",
                    "right nostril",
                    "hat",
                    "left trouser pocket",
                    "right trouser pocket",
                    "trendy turn-ups",
                    "!drink",
                    "!cheese",
                    "!bacon",
                    "!hangover",
                    "!bullshit",
                    "coffee",
                    "tea",
                    "notebook",
                    "left shoe",
                    "right shoe",
                    "mouth",
                    "top pocket"]

        self.finishes = ["and gets his coat",
                    "and takes a bow",
                    "and winks at Pambot",
                    "and winks at David",
                    "and leaves",
                    "and vanishes in a puff of smoke",
                    "and leaves through the trapdoor",
                    "and evaporates",
                    "and teleports to Swindon",
                    "and claps the tune of Blankety Blank",
                    "and pedals off on the tiny tricycle",
                    "and sniffs",
                    "and asks for honest feedback",
                    "and mumbles something about Debbie McGee in '89",
                    "and pours himself a !drink",
                    "and !ponders",
                    "and documents the process in a !prezi"]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        action = random.choice( self.actions )
        thing = random.choice( self.things )
        location = random.choice( self.locations )
        finish = random.choice( self.finishes )
        message_out = template.substitute( name=name, action=action, thing=thing, location=location, finish=finish)
        return "/me %s" % message_out











