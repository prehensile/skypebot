# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
## Also: Please indent using spaces.
class ExampleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("lobs a dolphin at $name.") ]
        self.command_mappings = [ "w3t", "splashy" ]
        self.enabled = False # change to True (or just delete this line) to enable a command

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class LoveCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "love" ]
        self.templates = [  Template("nuzzles $name."),
                            Template("slaps $name on the behind, winks."), 
                            Template("clumsily flirts with $name."), 
                            Template("invites $name for a threeway with Pambot."), 
                            Template("puts all his cards on the table. $name: I love you."), 
                            Template("sends $name a Valentine's ecard."), 
                            Template("asks $name out for a !drink.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
class BenchmarkCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "benchmark" ]
        self.templates = [  Template("compares $name to $name and declares a no contest."),
                            Template("compares $name to $name and declares a breakeven."), 
                            Template("is disappointed with $name’s fiscal performance."), 
                            Template("grabs his copy of “Six Sigma for Dummies."), 
                            Template("presents $name with a tiny financial breakdown."), 
                            Template("audits his suppliers."),
                            Template("does something in Excel."), 
                            Template("blames Marketing."), 
                            Template("thinks $name would perform better if $name outsourced $name’s drinking."), 
                            Template("puts on a super massive tiny suit."),
                            Template("tells $name to make a fucking appointment, just like $name did."), 
 
                            Template("whips out his calculator.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 
 
 
class StrategyCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "eno", "brian", "strategy", "oblique" ]
        self.templates = [ Template("reminds $name that $strategy"),
                Template("suggests that $name $strategy"),
                Template("nods sagely to $name, says $strategy"),
                Template("hints that $name may $strategy"),
                Template("tells $name to keep calm and $strategy"), 
                Template("ask $name if they're happy. Then asks, $query"), 
                Template("can relate to $name's problem; Landy solved it by asking himself $query"), 
                Template("asks $name to keep calm and $query") ]

        self.strategies = [ "A line has two sides.",  
            "A very small object. Its centre.",  
            "Abandon desire.",  
            "Abandon normal instructions.",  
            "Accept advice.",  
            "Adding on.",  
            "Always give yourself credit for having more than personality.",  
            "Ask people to work against their better judgement.",  
            "Ask your body.",  
            "Balance the consistency principle with the inconsistency principle.",  
            "Be dirty.",  
            "Be extravagant.",  
            "Breathe more deeply.",  
            "Bridges -- build -- burn.",  
            "Cascades.",  
            "Change ambiguities to specifics.",  
            "Change instrument roles.",  
            "Change nothing and continue consistently.",  
            "Children -- speaking -- singing.",  
            "Cluster analysis.",  
            "Consider different fading systems.",  
            "Consult other sources -- promising -- unpromising.",  
            "Convert a melodic element into a rhythmic element.",  
            "Courage!",  
            "Cut a vital connection.",  
            "Decorate, decorate.",  
            "Destroy nothing; Destroy the most important thing.",  
            "Discard an axiom.",  
            "Disciplined self-indulgence.",  
            "Discover your formulas and abandon them.",  
            "Display your talent.",  
            "Distort time.",  
            "Do nothing for as long as possible.",  
            "Do something boring.",  
            "Do something sudden, destructive and unpredictable.",  
            "Do the last thing first.",  
            "Do the washing up.",  
            "Don't avoid what is easy.",  
            "Emphasize differences.",  
            "Emphasize repetitions.",  
            "Emphasize the flaws.",  
            "Feed the recording back out of the medium.", 
            "Fill every beat with something.",  
            "Find a safe part and use it as an anchor.",  
            "Get your neck massaged.",  
            "Ghost echoes.",  
            "Give the name away.",  
            "Give way to your worst impulse.", 
            "Go outside. Shut the door.",  
            "Go slowly all the way round the outside.",  
            "Idiot glee.",  
            "Imagine the piece as a set of disconnected events.",  
            "Infinitesimal gradations.",  
            "Intentions -- nobility of -- humility of -- credibility of.",  
            "Into the impossible.",  
            "It is quite possible (after all).",  
            "Just carry on.",  
            "Left channel,right channel, center channel.",  
            "Listen to the quiet voice.",  
            "Look at the order in which you do things.",  
            "Lost in useless territory.",  
            "Lowest common denominator.",  
            "Magnify the most difficult details.", 
            "Make a blank valuable by putting it in an exquisite frame.",  
            "Make what's perfect more human.",  
            "Mechanize something idiosyncratic.",  
            "Mute and continue.",  
            "Only one element of each kind.",  
            "Openly resist change.",  
            "(Organic) machinery.",  
            "Put in earplugs.",  
            "Reevaluation (a warm feeling).",  
            "Remember quiet evenings.",  
            "Remove a restriction.",  
            "Repetition is a form of change.",  
            "Reverse.",  
            "Short circuit (example: a man eating peas with the idea that they will improve his virility shovels them straight into his lap).",  
            "Simple subtraction.",  
            "Spectrum analysis.",  
            "Take a break.",  
            "Take away the important parts.",  
            "Tape your mouth.",  
            "The inconsistency principle.",  
            "The tape is now the musix.",  
            "Think of the radio.",  
            "Tidy up.",  
            "Trust in the you of now.",  
            "Turn it upside down.",  
            "Twist the spine.",  
            "Use an old idea.",  
            "Use an unacceptable color.",  
            "Use fewer notes.",  
            "Use filters.",  
            "Use your own ideas.",  
            "Water.",  
            "Work at a different speed.",  
            "You are an engineer.",  
            "You can only make one dot at a time.",  
            "Your mistake was a hidden intention.",  
            "Don't break the silence.",  
            "Don't stress one thing more than another.",  
            "Use 'unqualified' people.",  
            "Try faking it.", 
            "Slow preparation, fast execution",  
            "Voice your suspicions.",  
            "Make it more sensual.",  
            "Use something nearby as a model.",  
            "Think -- inside the work -- outside the work",  
            "Go to an extreme, come part way back.",  
            "Once the search has begun, something will be found.",  
            "Be less critical.",  
            "From nothing to more than nothing.", 
            "Retrace your steps.",  
            "Only a part, not the whole.",  
            "Faced with a choice, do both.", 
            "Always give yourself credit for having more than personality.", 
            "Revaluation (a warm feeling).",  
            "Lost in useless territory.",  
            "It is quite possible (after all).", 
            "Idiot glee.",  
            "Move towards the unimportant.",  
            "It is simply a matter of work.",  
            "Not building a wall; making a brick.",  
            "The most easily forgotten thing is the most important.",  
            "State the problem as clearly as possible.", 
            "Always the first steps.",  
            "Question the heroic.",  
            "Go outside. Shut the door.",  
            "In total darkness, or in a very large room, very quietly.",  
            "Change specifics to ambiguities.", 
            "Use cliches.", 
            "Consider transitions" ]

        self.queries = [ "Which parts can be grouped?",
            "What context would look right?",  
            "When is it for?",  
            "What to increase? What to reduce? What to maintain?",  
            "How would someone else do it?", 
            "Would anyone want it?",  
            "What is the simplest solution?", 
            "Is the style right?",  
            "Where is the edge?",  
            "What wouldn't you do?",  
            "What are you really thinking about just now?",  
            "What is the reality of the situation?",  
            "What mistakes did you make last time?",  
            "What would your closest friend do?", 
            "What are the sections sections of? Imagine a caterpillar moving.", 
            "Is the intonation correct?",  
            "Is it finished?",  
            "Is something missing?",  
            "How would you have done it?.",  
            "Do the words need changing?",  
            "Do we need holes?" ]
            
    def generate( self, name ):
        strategy = random.choice(self.strategies)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, strategy=strategy)
        return "/me %s" % message_out
