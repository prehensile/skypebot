# coding=UTF-8

from string import Template
import random
import commandbase

class CoffeeCommand( commandbase.BaseCommand ):

    def __init__(self):
        
        self.templates = [  Template("stares at $name, disregards the order and serves an home-roasted espresso ristretto."),
                            Template("rolls his eyes, grabs the Aeropress and pours $name $coffee"),
                            Template("looks at $name disgusted and mumbles something about this being a bar and no fucking Starbucks."),
                            Template("smiles, pours $name $coffee and makes it Irish."),
                            Template("sticks a needle in the vein of $name and starts pouring $coffee into the IV."),
                            Template("opens the chminey door and roasts the beans before brewing $name $coffee."),
                            Template("grabs the V60 and falls into a trance while pouring $coffee for $name in slow, circular motions.")]
        
        self.pre_modifiers = [ "a steaming cup of",
                   "some slowly dripped",
                   "a fine blend of",
                   "a freshly brewed mug of",
                   "a shot of",
                   "a lukewarm mug of preheated",
                   "an iced glass of"]              

        self.coffees = [ "Espresso",
                    "Nepal Mount Everest Supreme",
                    "Brazil Washed Fazenda da Lagoa",
                    "Ecuador washed Galapagos Isle",
                    "Jamaica Blue Mountain",
                    "Organic Ethiopia Yirgacheffe Adado",
                    "Organic Indonesia Gajah Aceh",
                    "Decaf Santa Ana Espresso"]

        
    def generate( self, name ):
        coffee = random.choice( self.coffees )
        pre_modifier = random.choice( self.pre_modifiers )
        coffee = "%s %s" % (pre_modifier, coffee)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, coffee=coffee)
        return "/me %s" % message_out
