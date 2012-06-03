# coding=UTF-8

from string import Template
import random

update_messages = [
    Template( "/me goes glassy eyed for a moment as an update is recieved. If he doesn't come back it's $name's fault." ),
    Template( "/me runs from the bar, screaming something about $name and an update." ),
    Template( "/me bursts into the cubicle in real need of a slash. $name is caught with their pants down." ),
    Template( "/me rings the bell - the $name updates are here. Get your updates." ),
    Template( "/me spills the gossip, $name was caught fiddling in the back a minute ago." )
]

new_chat_messages = [
    "/me re-appears a split nanosecond after his ratty carpet slippers do.",
    "/me rides in on a tiny tricyle.",
    "/me tells Gregory Povey it’s okay to post now."
]

def update_message_for_name( name ):
    template = random.choice( update_messages )
    return template.substitute( name=name )

def new_chat_message():
    message = random.choice( new_chat_messages )
    return( message )
