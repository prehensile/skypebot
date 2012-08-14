# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class LspCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "lsp" ] 


        self.wisdom = [ 
            "I\'m in my bedroom.",
            "I can see ice and snow .",
            "What goes on.",
            "What can you see?",
            "Maybe you are, who knows.",
            "Maybe you have double vision.",
            "An average day is like the sun shining and it\'s nice and you can see clouds flying and things like that.",
            "On a rainy day, on a winter\'s day, you stay indoor depending on what your mood is like.",
            "I describe my personality as like an animal among cannibals.",
            "I don\'t like to say that I\'m a man, because I don\'t want to be a man.",
            "I think I\'m an angel.",
            "They do things that the devil do.",
            "Understand? Understand when I was a man I was a cannibal.",
            "I decide not to be a man, I want to be an angel, so I don\'t eat what the man eat.",
            "I don\'t smoke what the man smoke.",
            "So I stop smoke.",
            "I stop eating what man eat.",
            "I stop eat fish, I stop eat meat.",
            "I stop eat like an animal.",
            "I don\'t smoke any more because I wish to be healthy.",
            "So what man do I don\'t do any more.",
            "I do different.",
            "I like broccoli, I like cabbage, calalou, choko and others.",
            "I drink orange juice, I eat banana.",
            "Brown banana, green banana, whatever banana it is, I like it.",
            "My wife needs money, and she has a lot of bills to get paid, and I will have to help her pay the bills.",
            "Lot of people believe in God but they are not aware of God.",
            "God is alive and God is coming like a thief in the night [chuckles again].",
            "You know God don\'t tell no one when he is coming.",
            "It could be a couple years, it could be three years, five, it could be 10.",
            "That\'s the idea.",
            "My wife love luxury, she loves money.",
            "She loves good food, she always wants to eat in good restaurants, and the shoes, the best clothes, the best everything.",
            "See, I believe in less, but my wife believe in best.",
            "She believe in vanity.",
            "I look upon it from a balance point of view because if it wasn\'t for tax so many people die because some people don\'t have job.",
            "It a little bit rough and tough without the tax.",
            "Half the world would be eating and drinking, and the other half would die beause they wouldn\'t have anything.",
            "It\'s ok for me, it\'s a little bit tough but somebody have to help somebody.",
            "My music is for people who believe in god.",
            "So if people believe in God this is what my music can do for them.",
            "The people believe in Jesus Christ, it can help them.",
            "But if they believe in the AntiChrist it cannot help them.",
            "People who believe in God make music will hear positive words, perfect love and it will heal their soul.",
            "If they believe in the devil it can\'t help them.",
            "Well, the Super Ape to me is an image.",
            "And the image, we all in the belly of the Super Ape.",
            "The interpretation of the Super Ape is in the Super Space.",
            "The army, the sky, the firmament are in the image of the Super Ape.",
            "So we are living in the Super Ape.",
            "The Super Ape is all the galaxy.",
            "All the comets of the universe.",
            "Dubstep is all right because that\'s when me start to walk like the Super Ape.",
            "Man start fear and the people just start to move towards it, because of the declaration of monster.",
            "Monster walk, monster dance, monster shake, monster rock and that\'s what goes on.",
            "Dubstep Super Ape dubstep this dubstep that, it\'s all like machine, robot affair.",
            "Monster robots, yeah?",
            "That you have a father inside of you.",
            "The church try not to tell you, but you yourself are the church and our Father who art in heaven is in you.",
            "Heaven is in the Father, and heaven is in you because the Father creates you.",
            "So when you pray and you say \'our Father who art in heaven\' instead of saying Our Father say Our Farter.",
            "Yes.",
            "Because God give you the breath of life and it goes into you.",
            "Later what goes into you wants to go outside.",
            "So when it wants to go outside it means a fart.",
            "Our father give you the breath of life and when it want to go outside it go \'pooooo\'! That a farting noise.",
            "And poo is really good to make music for the bass line.",
            "And the bassline is like \'poo, poo, pooopooo poo\' or something like that.",
            "The breath of life is fresh air.",
            "The message is that you can see yourself as a Son of God, see yourself as a King of God see yourself as a Prince of God.",
            "Do your prior, do your exercise and buy the food and eat it and the drink.",
            "Don\'t smoke too much, you destroy your lungs.",
            "You disrespect yourself and you become sick: all the bacteria and the virus and all them tings.",
            "All that cause virus and bacteria ? I stop doing them.",
            "I respect myself like God.",
            "When the time come when you have to stop smoke, you can drink it.",
            "You can make soup with it, you can make tea with it and make other things.",
            "Like soup.",
            "Treat it like a present or a treasure.",
            "A lot of people take herbs, but if a lot of people take this herb, then there wouldn\'t be the riots.",
            "Drink it.",
            "Or you could eat it like a vegetable.",
            "Or something like that.",
            "One love.",
            "I wasn\'t involved in anything with colonial government business.",
            "I have my own music government, black supremacy, Ethiopia family, Africa family, Addis Ababa, something like that.",
            "All the riches of the earth is black.",
            "The isle is black.",
            "When they came and see the isle they brought the vampire with them to eat the children\'s blood, they hijacked them and they lowjacked them...",
            "Do you have a tape machine running?",
            "That\'s very good.",
            "The old fella sings a cappella and he took his umbrella and here comes the lightning flash, KNNNNNARARCARHHHH.",
            "It flashed for the government exterminator, the high priest become low priest and then low beast, moo cow HOOOOOWARGHhhhhh.",
            "Nahhhh.",
            "It\'s coming shortly! Fire government, water government, flood government.",
            "It\'s coming soon...!",
            "I will be coming to you from fire fire fire fire! Super hot hot hot! Here comes the jungle god! Lee Scratch Perry on the wire!",
            "A few people will be gods and goddesses and angels! And the others all kaput! Great balls of fire...",
            "WAAAAAARGHHH!",
            "Cosmic energy telepathic all the time!",
            "In my music.",
            "Back in Jamaica!",
            "Independence! I don\'t want no white coat, I don\'t want no white goat! Baaaa baaaa! This is the future speaking! I feel the telepathic power! I was born 1936.",
            "Nine nine nine, I never changed my mind.",
            "I have the hot line...",
            "why should I die, I\'m not eating dead mwaah, I\'m not eating dead moooo, why should I die? I was travelling from BC to AD when you called.",
            "I\'m in my black coat.",
            "My mission is secret.",
            "Secret number 9.",
            "Nine nine nine...",
            "so that\'s my news on independence! Hahahahahahahahah..."]
        

        self.templates = [  Template("advises $name: "),
                            Template("imparts wisdom: "),
                            Template("drops the truth on $name: ")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        quote = random.choice( self.wisdom );
        message_out = template.substitute(name=name)+"\""+quote+"\"";
        return "/me %s" % message_out
