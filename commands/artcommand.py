# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ArtCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "art" ]
        self.templates = [  Template("paints a picture of Morrissey."),
                            Template("something something algorithmic portraits."),
                            Template("daubs $name in paint."), 
                            Template("applies for some funding."), 
                            Template("gets naked and rolls around."),
                            Template("screams into $name's face, calls it an intervention."),
                            Template("paints his fingernails."),
                            Template("is playing with time-based media."),
                            Template("has a site-specific work commission."),
                            Template("is sticking out of Teddy's arse."),
                            Template("disappoints his parents."),
                            Template("has daddy issues."),
                            Template("sticks a poet through a voice synth."),
                            Template("Markovs some poetry."),
                            Template("bleeds for his !art."),
                            Template("has daddy issues."),
                            Template("builds an installation of different-sized dongs."),
                            Template("is running a pop-up craft shop."),
                            Template("incorporates the self into the work."),
                            Template("believes that $name represents the most degenerate of Western !Art."),
                            Template("works part-time in a bar to pay his rent."),
                            Template("makes a plaster cast of $name's arse."),
                            Template("sells some old shit to a posh twat."),
                            Template("paints a lovely picture of $name then sets it on fire."),
                            Template("wonders why he's so poor."),
                            Template("strops off saying 'you just don't understand me!'"),
                            Template("makes a preparatory sketch."),
                            Template("asks you to take all your clothes off and lie over there."),
                            Template("cuts off his ear and posts it to pambot."),
                            Template("drinks too much absinthe and gets punchy."),
                            Template("wears a smock."),
                            Template("paints it black."),
                            Template("makes some street art, yeah?"),
                            Template("tries to work out what to rip off next"),
                            Template("cleans his brushes"),
                            Template("loses an eye in a duel"),
                            Template("abandons his family and moves to a tropical island"),
                            Template("exhibits at the white cube"),
                            Template("invites you to his PV.") ] 

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 