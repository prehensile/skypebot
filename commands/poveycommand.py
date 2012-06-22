# coding=UTF-8

from string import Template
import random
import commandbase

class PoveyCommand( commandbase.BaseCommand ):

    def __init__(self):
        self.command_mappings = [ "povey" ]
        self.templates = [  Template("thinks $name completes him."),
                            Template("nurtures a hangover."),
                            Template("organises a conference"),
                            Template("makes some badges"),
                            Template("puts Side B on."),
                            Template("could go for a nap quite happily."),
                            Template("wangs all his money on Drawn & Quarterly."),
                            Template("writes an erotic ebook."),
                            Template("congratulates $name."),
                            Template("makes a shit pun."),
                            Template("as uttered forth in the public works of Puncher and Wattmann of a personal God quaquaquaqua with white beard."),
                            Template("corrects !marcus' spelling."),
                            Template("instagrams the cat."),
                            Template("forgot to add a mapping."),
                            Template("automagically grows a beard"),
                            Template("buggers off to Denmark for a bit."),
                            Template("nips out the back to catch up with the wrestling"),
                            Template("was on the best seat in the bus this morning"),
                            Template("calls $name a divvy")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out