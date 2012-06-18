# coding=UTF-8

from string import Template
import random

incoming_status_templates = [
    Template( "/me stiffens as $name thumps on the wall and yells something \
about $message." ),
    Template( "/me digs out the phone from under a pile of empties, listens for \
a second then yells out something about $name and $message." ),
    Template( "/me chases $name away from the windows with a broom. They yell \
something about $message over their shoulder in parting." ),
    Template( "/me finds $name hiding in the bogs, mumbling something about \
$message." ),
    Template( "/me catches a brick as it flies in through a front window. \
There's a note wrapped around it from $name. The crayon is badly \
smudged, but it's possible to make out something about $message." )
    Template( "/me gets pocket-dialled by $name. In the background, he can work out \
bits of a broken $message." )
]

muffle_words = [ "something", "blah", "yadda" ]

def message_for_incoming_status( status ):
    text = status.text
    words = text.split(" ")
    if len( words ) > 1 :
        # strip leading @replies
        if words[0].startswith( "@" ):
            words = words[1:]
        # muffle text
        muffle_amount = 0.4 # muffle a 40% of input words
        num_words = len(words)
        # get a list of references to status words
        indexes = range( 0, num_words-1 )
        # randomise list of references
        random.shuffle( indexes )
        # replace words from the input text referred to by the 
        # first muffle_amount percentage of references
        for i in range( 0, int(num_words * muffle_amount) ):
            index = indexes[ i ]
            words[ index ] = random.choice( muffle_words )
        message = " ".join( words )
        # remove trailing punctuation from message
        message = message.rstrip(".?!")
        # get author name
        name = "@%s" % status.author.screen_name
        # choose a template
        template = random.choice( incoming_status_templates )
        return template.substitute( name=name, message=message )
    return None


