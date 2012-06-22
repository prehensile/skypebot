# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class HatCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "hat" ]
        self.templates = [ Template("chucks $name a $hat"),
                   Template("wonders where !dave got that nice $hat."),
                   Template("rolls a $hat down his arm, like what Michael Jackson did before he died."),
                   Template("gives $name a fusty, moth-bitten $hat from lost property."),
                   Template("rummages around in the dressing-up box and produces a battered $hat for $name"),
                   Template("knocks up a quick $hat for $name using his mad millinery skills.") ]
        
        self.hats = ['Akubra', 'Beanie', 'Beret', 'Boater', 'Busby', 'Capuchon', 'Chupalla', 'Deerstalker',
        'Fedora', 'Kepi', 'Kippah', 'Jew', 'Kufi', 'Nasaq', 'Inuit', 'Pakol', 'Rogatywka', 'Salakot',
        'Skullcap', 'Sombrero', 'Trilby', 'Tubeteika', 'Tuque', 'Turban', 'Ushanka', 'Zucchetto',
        'Bicorne', 'Bycoket', 'Capotain', 'Caubeen', 'bicorne', 'Deerstalker', 'Kolpik', 'Peci',
        'Papakha', 'Shtreimel', 'Spodik', 'Sombrero', 'Pope', 'Mitre', 'Tricorne', 'Trilby',
        'Capotain', 'Hennin', 'Kokoshnik', 'Vietnam', 'Vietnam', 'Ochipok', 'Tantour', 'Copintank',
        'Cordies', 'Cossack', 'Crinoline', 'Singapore', 'Jaapi', 'Kausia', 'Kevenhuller', 'Montera',
        'Mousquetaire', 'Petasos']

    def generate( self, name ):
        template = random.choice( self.templates )
        hat = random.choice( self.hats )
        message_out = template.substitute( name=name, hat=hat )
        return "/me %s" % message_out