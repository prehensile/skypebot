# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class LoveCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "love" ]
        self.templates = [  Template("nuzzles $name."),
                            Template("slaps $name on the behind, winks."), 
                            Template("clumsily flirts with $name."), 
                            Template("invites $name for a threeway with Pambot."), 
                            Template("puts all his cards on the table. $name: I love you."), 
                            Template("sends $name a Valentine's ecard."), 
                            Template("gives $name a single red rose."), 
                            Template("drunk dials $name."), 
                            Template("ties a cherry stem with his tongue."), 
                            Template("gives $name a sensual massage."), 
                            Template("puts some Barry White on for $name."), 
                            Template("takes $name out for dinner and a movie."), 
                            Template("puts on a pair of suspenders for $name."), 
                            Template("breaks into $name's house and leaves a box of Milk Tray."), 
                            Template("hits up $name for a booty call."), 
                            Template("lays $name down on the sheepskin rug by the fire."), 
                            Template("caresses $name's !hands."), 
                            Template("bakes a soufflé."), 
                            Template("chokes on an oyster."), 
                            Template("bought the expensive chocolate."), 
                            Template("caught something from $name."), 
                            Template("asks if that is a teddy in $name's pocket, or if they're just pleased to see him."), 
                            Template("looks longingly into $name's eyes."), 
                            Template("does a sexy fan dance for $name."),
                            Template("is wearing a peephole bra."),
                            Template("writes a sonnet."),   
                            Template("simply says '$name, I love you' "),
                            Template("shoots Cupid's arrow at $name"),  
                            Template("asks $name out for a !drink.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out