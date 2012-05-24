from string import Template
import random

class CoffeeCommand(object):

	def __init__(self):
		
		self.templates = [ 	Template("stares at $name, disregards the order and serves an home-roasted espresso ristretto."),
		 					Template("rolls his eyes, grabs the Aeropress and pours $name $coffee"),
							Template("looks at $name disgusted and mumbles something about this being a bar and no fucking Starbucks."),
							Template("smiles, pours $name $coffee and makes it Irish.")]
		
		self.pre_modifiers = [ "a steaming cup of",
				   "some slowly dripped",
				   "a fine blend of",
				   "a freshly brewed mug of",
				   "a shot of",
				   "a lukewarm mug of preheated"]				

		self.coffees = [ "Espresso",
					"Nepal Mount Everest Supreme",
					"Brazil Washed Fazenda da Lagoa",
					"Ecuador washed Galapagos Isle",
					"Jamaica Blue Mountain",
					"Organic Ethiopia Yirgacheffe Adado",
					"Organic Indonesia Gajah Aceh",
					"Decaf Santa Ana Espresso"]

		
	def execute( self, message ):
		coffee = random.choice( self.coffees )
		pre_modifier = random.choice( self.pre_modifiers )
		coffee = "%s %s" % (pre_modifier, coffee)
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, coffee=coffee)
		return "/me %s" % message_out
