# coding=UTF-8
from string import Template
import random
import commandbase

class HangoverCommand( commandbase.BaseCommand ):

    def __init__(self):
        self.templates = [ Template("is still wearing yesterday's clothes."),
                           Template("doesn't smell so good."),
                           Template("has bags on the bags under his 'eyes'."),
                           Template("gazes off into space."),
                           Template("forgets what he was saying."),
                           Template("sneaks off for a nap."),
                           Template("is running on !coffee & painkillers."),
                           Template("bangs on about Irn Bru."),
                           Template("!bacon !bacon !bacon"),
                           Template("would rather not talk about it.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out