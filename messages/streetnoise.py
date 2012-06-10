# coding=UTF-8

from string import Template
import random

incoming_status_templates = [
    "/me stiffens as $name thumps on the wall and yells something about $message.",
    "/me digs out the phone from under a pile of empties, listens for a second then yells out something about $name and $message.",
    "/me chases $name away from the windows with a broom. They yell something about $message over their shoulder in parting.",
    "/me finds $name hiding in the bogs, mumbling something about $message."
]

muffle_words = [ "something", "worple", "blah" ]

def message_for_incoming_status( status ):
    # muffle text
    muffle_amount = 0.3 # muffle a third of input words
    words = status.text.split(" ")
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
    message.rstrip(".?!")
    # get author name
    name = "@%s" % status.author.screen_name
    # choose a template
    template = random.choice( incoming_status_templates )
    return template.substitute( name=name, message=message )


