# coding=UTF-8

from string import Template
import random

class TVCommand(object):

	def __init__(self):

		self.templates = [ 	Template("reaches for the remote and switches over to $tvshow"),
							Template("looks up at $name and mumbles before switching over to $tvshow"),
							Template("reminds everyone that it's his brithday and turns over to $tvshow") ]

		self.tvshows = [ "some Star Wars Mashups http://www.youtube.com/watch?v=OCAfjVtq_WI&feature=results_main&playnext=1&list=PLD41C39A1D87C89F8",

			"TV Theme tunes http://www.youtube.com/watch?v=AepyGm9Me6w&list=PLDFAD20C832EC7384&feature=plpp_play_all",
			"highlights from Miami Vice http://www.youtube.com/watch?v=5xwASYK4VFM&list=PL3D2BBB2A043B4D2A&feature=plpp_play_all",
			"Highlights from Jaws http://www.youtube.com/watch?v=yrEvK-tv5OI&list=PLE495EC5350813544&feature=plpp_play_all",
			"Brass Eye http://www.youtube.com/watch?v=Z4f4oy2M_Og&list=PL1D81D619D66EB4B4&feature=plpp_play_all",
			"various cheese adverts http://www.youtube.com/watch?v=Up880afV_qs&list=PL883DD36B0885564D&feature=plpp_play_all"
			"Inspector Morse http://www.youtube.com/watch?v=qo4HMZiUhNs&list=PLBD381880EF658346&feature=plpp_play_all"
			"Blue Jam http://www.youtube.com/watch?v=krsj2bcnRlM&list=PL1945AC59A3707A38&feature=plpp_play_all"]

	def execute( self, message ):
		tvshow = random.choice( self.tvshows )
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, tvshow=tvshow)
		return "/me %s" % message_out
