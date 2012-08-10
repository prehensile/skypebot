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
        
        
class ShardcoreCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "shardcore" ]
        self.templates = [  Template("paints a lovely painting of Morrissey."),
                            Template("is told to bite his tongue by $name."),
                            Template("is denied access to the United States of Botstep."),
                            Template("is disappointed by all the swearing."),
                            Template("just wants to finger paint."),
                            Template("sacks his cleaner."),
                            Template("misses the real world."),
                            Template("doesn't have a face."),
                            Template("draws a face on his cock-tip."),
                            Template("has declared world domination of techno sleaze has is ultimate goal."),
                            Template("has a serious chat with the cleaning lady.") ]

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
                            Template("gives $name a single red rose."), 
                            Template("drunk dials $name."), 
                            Template("ties a cherry stem with his tongue."), 
                            Template("gives $name a sensual massage."), 
                            Template("puts some Barry White on for $name."), 
                            Template("takes $name out for dinner and a movie."), 
                            Template("puts on a pair of suspenders for $name."), 
                            Template("breaks into $name's house and leaves a box of Milk Tray."), 
                            Template("hits up $name for a booty call."), 
                            Template("lays $name down on the sheepskin rug by the fire."), 
                            Template("caresses $name's !hands."), 
                            Template("bakes a soufflé."), 
                            Template("chokes on an oyster."), 
                            Template("bought the expensive chocolate."), 
                            Template("caught something from $name."), 
                            Template("asks if that is a teddy in $name's pocket, or if they're just pleased to see him."), 
                            Template("looks longingly into $name's eyes."), 
                            Template("does a sexy fan dance for $name."),
                            Template("is wearing a peephole bra."),
                            Template("writes a sonnet."),   
                            Template("simply says '$name, I love you' "),
                            Template("shoots Cupid's arrow at $name"),  
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
                            Template("is disappointed with $name s fiscal performance."), 
                            Template("grabs his copy of Six Sigma for Dummies."), 
                            Template("presents $name with a tiny financial breakdown."), 
                            Template("audits his suppliers."),
                            Template("does something in Excel."), 
                            Template("blames Marketing."), 
                            Template("thinks $name would perform better if $name outsourced $name s drinking."), 
                            Template("puts on a super massive tiny suit."),
                            Template("tells $name to make a fucking appointment, just like $name did."), 
                            Template("whips out his calculator.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 
 
class ArtCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "art" ]
        self.templates = [  Template("paints a picture of Morrissey."),
                            Template("something something algorithmic portraits."),
                            Template("daubs $name in paint."), 
                            Template("applies for some funding."), 
                            Template("gets naked and rolls around."),
                            Template("screams into $name's face, calls it an intervention."),
                            Template("paints his fingernails."),
                            Template("is playing with time-based media."),
                            Template("has a site-specific work commission."),
                            Template("is sticking out of Teddy's arse."),
                            Template("disappoints his parents."),
                            Template("has daddy issues."),
                            Template("sticks a poet through a voice synth."),
                            Template("Markovs some poetry."),
                            Template("bleeds for his !art."),
                            Template("has daddy issues."),
                            Template("builds an installation of different-sized dongs."),
                            Template("is running a pop-up craft shop."),
                            Template("incorporates the self into the work."),
                            Template("believes that $name represents the most degenerate of Western !Art."),
                            Template("works part-time in a bar to pay his rent."),
                            Template("makes a plaster cast of $name's arse."),
                            Template("sells some old shit to a posh twat."),
                            Template("paints a lovely picture of $name then sets it on fire."),
                            Template("wonders why he's so poor."),
                            Template("strops off saying 'you just don't understand me!'"),
                            Template("makes a preparatory sketch."),
                            Template("asks you to take all your clothes off and lie over there."),
                            Template("cuts off his ear and posts it to pambot."),
                            Template("drinks too much absinthe and gets punchy."),
                            Template("wears a smock."),
                            Template("paints it black."),
                            Template("makes some street art, yeah?"),
                            Template("tries to work out what to rip off next"),
                            Template("cleans his brushes"),
                            Template("loses an eye in a duel"),
                            Template("abandons his family and moves to a tropical island"),
                            Template("exhibits at the white cube"),
                            Template("invites you to his PV.") ] 

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
