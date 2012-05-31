# coding=UTF-8
from string import Template
import random

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
class ExampleCommand(object):

	def __init__(self):
		self.templates = [ 	Template("lobs a dolphin at $name.") ]

	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
		
class HatCommand(object):

	def __init__(self):
		self.templates = [ Template("chucks $name a $hat"),
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

	def execute( self, message ):
		name = message.FromDisplayName
		template = random.choice( self.templates )
		hat = random.choice( self.hats )
		message_out = template.substitute( name=name, hat=hat )
		return "/me %s" % message_out
		