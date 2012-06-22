# coding=UTF-8
from string import Template
import random
import commandbase

class HangoverCommand( commandbase.BaseCommand ):

    def __init__(self):
      self.command_mappings = [ "hangover" ]
      self.templates = [ Template("is still wearing yesterday's clothes."),
                           Template("doesn't smell so good."),
                           Template("has bags on the bags under his 'eyes'."),
                           Template("gazes off into space."),
                           Template("forgets what he was saying."),
                           Template("sneaks off for a nap."),
                           Template("glazes over."),
                           Template("has been sitting in someone else's seat for ten minutes without realising it."),
                           Template("burped and tasted a forgotten late-night kebap."),
                           Template("is wearing his boxers back to front."),
                           Template("blames !satan."),
                           Template("weeps emotionally over nothing in particular."),
                           Template("asks everyone if they could just... shh a bit."),
                           Template("is running on !coffee & painkillers."),
                           Template("bangs on about Irn Bru."),
                           Template("!bacon !bacon !bacon"),
                           Template("would rather not talk about it.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out