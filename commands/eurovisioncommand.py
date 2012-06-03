# coding=UTF-8

from string import Template
import random

class EurovisionCommand(object):

    def __init__(self):

        self.templates = [  Template("gives $name $points points."),
                        Template("sides with $name's rival. Everyone agrees it's bloc politics."),
                        Template("mutes the channel as $name's country performs."),
                        Template("loses the results."),
                        Template("goes crazy with the hashtag. #esc2012 #time #cock #terry"),
                        Template("dons an obvious wig and says something wry about $name's entry."),
                        Template("can't help staring at $name's tits in their slightly mutton dress."),
                        Template("pours another !drink as $country perform."),
                        Template("knows all the words to Woki Mit Deim Popo, Austria's entry."),
                        Template("is having trouble on the line."),
                        Template("ignores a prat in the background trying to get on telly. Turns out it was $name."),
                        Template("is wearing his most sequinned jacket."),
                        Template("remembers when we would win it every year, then let the Irish have it."),
                        Template("still has complicated feelings about Dana International."),
                        Template("speeds it up, then he slows it down."),
                        Template("is shocked by $name. Awards them nil points."),
                        Template("loves the national dress that $name is wearing."),
                        Template("breaks out in laughter as $name's backing dancers move out of sync."),
                        Template("turns his cap backwards, does a rap."),
                        Template("sings a heart-warming song about the struggles during the civil war. Goes Europop."),
                        Template("is wearing leather."),
                        Template("stands up off his seat as the key change kicks in."),
                        Template("singed his hair on the stage pyrotechnics."),
                        Template("waves a tiny $country flag."),
                        Template("switches into English for the chorus."),
                        Template("misses Gina G."),
                        Template("flashes his gusset in a desperate attempt for douze points."),
                        Template("duffs up his vocals. Sings 'ooh ooh ooh' to cover."),
                        Template("references the host nation to cover his forgetten lyrics."),
                        Template("breaks down."),
                        Template("makes an amusingly jingoistic comment about $country"),
                        Template("raids the liquor cabinet for some !drink to take the pain away from $name's awful singing."),
                        Template("is all smiles as $name awards $country $points.")
                        ]
                            
        self.country = [ "Albania",
            "Armenia",
            "Austria",
            "Azerbaijan",
            "Belarus",
            "Belgium",
            "Bosnia and Herzegovina",
            "Bulgaria",
            "Croatia",
            "Cyprus",
            "Denmark",
            "Estonia",
            "Finland",
            "France",
            "Georgia",
            "Germany",
            "Greece",
            "Hungary",
            "Iceland",
            "Ireland",
            "Israel",
            "Italy",
            "Latvia",
            "Lithuania",
            "Macedonia",
            "Malta",
            "Moldova",
            "Montenegro",
            "Netherlands",
            "Norway",
            "Poland",
            "Portugal",
            "Romania",
            "Russia",
            "San Marino",
            "Serbia",
            "Slovakia",
            "Slovenia",
            "Spain",
            "Sweden",   
            "Switzerland",
            "Turkey",
            "Ukraine",  
            "United Kingdom"]
        
    def execute( self, message ):
        name = message.FromDisplayName
        points = "%d" % random.randint( 0, 12 )
        country = random.choice( self.country )
        template = random.choice( self.templates )
        message_out = template.substitute( name=name, points=points, country=country )
        return "/me %s" % message_out
