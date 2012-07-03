# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class TwocentsCommand( BaseCommand ):

    def __init__(self):
    
        BaseCommand.__init__( self )
        
        self.command_mappings = [ "advice", "8ball", "fortune", "twocents", "tip", "warning", "word" ]
        
        self.templates = [  Template("reminds $name that to doubt would be an insult. a crime of existence."),
                    Template("opens his eyes after a long pause, tells $name, manifestation, doesn’t just mean physical ... stupid!" ),
                    Template("'s eyes roll back in his head, speaks in a voice not his own. Flow of futures grasp, merges closer to decay pivot of present."),
                    Template("lights a !drink on fire for $name. Mutters, fuel the future by capturing the past."),
                    Template("astrally projects himself. A voice emanates from above. Removing one factor could be an option of choice, but to do so will negate action on the indirect feedback loop of desire."),
                    Template("grabs $name by the shirt, spittle flying. Ideas are memories of the future, dammit!"),
                    Template("beckons $name closer and whispers in a conspiratorial tone, complacency of what is, is the stasis of existence."),
                    Template("levitates above the bar in the lotus position, surrounded by a glowing aura. Respect for what is, is the recognition of progress."),
                    Template("'s voice echoes in $name's inner eye. no one else hears. Persistence in what is, is the conflict of requirement."),
                    Template("slaps some sense into $name. Is it really needed to done? stop! is it really needed to not be done? go!"),
                    Template("opens his switchblade and challenges $name to a !rumble. Bellows, risk is safety forming into pauses of progress."),
                    Template("shakes his heads hopelessly at $name. Doubt for safety is witnessing stupidity. safe now. suffocating in risk later."),
                    Template("repeats enigmatically, < | > past < becoming < emerging < being > emerging > begoing > future < | >"),
                    Template("pulls out a Go board, challenges $name, says, on disagreement start the game. find along the way urgency to decide thoughts."),
                    Template("points $name to the loo. Calls after them, Explore entrances to points of no return for phases upgrading."),
                    Template("makes a mobius strip. hands it to $name. written on it is - Anytime has no boundaries as the loop is indistinguishable."),
                    Template("confers with !satan. Does $name really think it’s good to reduce that to something?"),
                    Template("chortles at $name's naievety. It's funny how people don't realise that 'now' is the best time.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out