# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class HeckleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("liked this better when no-one had heard of it."),
                            Template("thinks $name has totally sold out."),
                            Template("shouts at $name to get knob out."),
                            Template("demands $name plays some crust."),
                            Template("reckons that $name is talking out of their arse."),
                            Template("saw the original version at TEDxPhactory."),
                            Template("is unimpressed by $name's slide transition."),
                            Template("can't hear what $name is saying."),
                            Template("something something mumblecore what?"),
                            Template("laughs as $name's embedded YouTube video buffers loads."),
                            Template("mutters something about pinging bricks and casts a wry glance at $name."),
                            Template("links to the work $name referenced, explains how they have totally misrepresented it."),
                            Template("tweets '$name has SMEBS' on the official backchannel."),
                            Template("thinks $name is talking a load of post-whatsit !bullshit."),
                            Template("doesn't think much of $name's !handwork") ]
        self.command_mappings = [ "heckle" ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
