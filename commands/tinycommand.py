# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class TinyCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "tiny" ]
        self.templates = [  Template("shrinks the kids."),
                            Template("looks at $name through some binoculars."),
                            Template("squeezes the web into a size zero."), 
                            Template("throws $name out of the bar for being too big."),
                            Template("chuckles as $name disappears through the cracks in the floorboards."),
                            Template("appears to have been in some very cold water."),
                            Template("is all tilt-shifted and that."),
                            Template("is wearing a size 4 shoe."),
                            Template("declares that size doesn\'t matter as long as it\'s tiny"),
                            Template("shrinks $name and injects them into the blood stream of !satan."),
                            Template("is worried about quantum effects"),
                            Template("is swept up in a tsunami of brownian motion"),
                            Template("is the smallest human being, a microscopic man, he can do all the things the micro-man can"),
                            Template("is swept up in a tsunami of brownian motion"),
                            Template("shrinks $name in the hot wash"),
                            Template("rides in on a flea"),
                            Template("hides from the big kids on the big web"),
                            Template("takes $name into a secret room, even tinier than this one"),
                            Template("complains that this matchbox is too roomy"),
                            Template("dances to Ant Music.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out