# coding=UTF-8

from string import Template
import random

class ChoonCommand(object):

	def __init__(self):

		self.templates = [ 	Template("does a rubbish swan-dive and puts on some $choon for $name"),
							Template("slides along the bar and points at $name. Obviously, it has to be $choon"),
							Template("puts on the bestof $choon DVD. Noting this is totally $name."),
							Template("turns off all the lights and leaves you all with $choon."),
							Template("turns on the disco floor and plays $choon."),
							Template("appears dressed as $name just as the speakers blurt out $choon."),
							Template("jumps in through the window to the sound of $choon."),
							Template("pats $name on the back and heads to the bar - $choon plays quietly in the background"),
							Template("clicks his fingers and $choon brings the stereo alive again"),
							Template("would like to remind $name what happen last time when we had $choon on the radio."),
							Template("laughs at $name's dress code and pops $choon on the steampunk gramaphone"),
							Template("shouts to everyone this (mooning) is not a laughing matter and puts on $choon"),
							Template("walks in wearing $name's slippers and plays $choon"),
							Template("comes out from the cupboard with Pambot and quickly plays $choon"),
							Template("high 5's $name and puts on $choon"),
							Template("glares at @topfife and $name and reluctanty plays $choon"),
							Template("points out that he's on the phone ordering more cheese."),
							Template("shouts up that he's in the cellar and for $name to play $choon"),
							Template("reminds $name that it's his turn to choose $choon"),
							Template("scoffs at $name's hiphop favourites and serves up $choon"),
							Template("walks in wearing $name's sunglasses and serves up $choon"),
							Template("pops up behind the bar just as the stero blurts out $choon"),
							Template("sighs and plays $choon"),
							Template("crys and plays $choon"),
							Template("opens the windows as the volume comes up on $choon"),
							Template("winks at $name and plays $choon"),
							Template("glares at Marcus and Greg and grins, slipping on $choon"),
							Template("looks blankly at $name and plays $choon"),
							Template("cranks up the volume for $choon"),
							Template("plays 10seconds of $choon"),
							Template("plays $choon and backflips out of the bar"),
							Template("puts on $choon and pours himself a murky pint"),
							Template("switches over to $choon and pours himself a glitchy whisky"),
							Template("plays $choon and pours himself a glitchy sherry"),
							Template("plays $choon and pours himself a glitchy whisky"),
							Template("plays $choon and salutes you all"),
							Template("puts on the DVD of $choon and heads to the toilet"),
							Template("winks at Pambot and plays $choon"),
							Template("gives $name a dry slap plays $choon to teach him a lesson"),
							Template("backspins along the bar and asks $name to put on $choon") ]

		self.choons = [ "a massive slap of techno http://www.last.fm/tag/techno/tracks",
			"the best in classic (rock) rock http://www.last.fm/tag/classic+rock/tracks",
			"smooth 8-) jazz 8-) sax http://www.last.fm/tag/saxophone+jazz",
			"a bucket of 5pl45y mischief http://www.last.fm/tag/seapunk",
			"some mental (bandit) acid http://www.last.fm/tag/acid%20house/tracks",
			"some creepy shit (poolparty) http://www.last.fm/tag/haunting/tracks",
			"some hip swinging broadway (dance) (dance) (dance) (dance) (dance)  http://www.last.fm/tag/showtunes/tracks",
			"some fine rare Norse groove http://www.last.fm/music/I+Shot+The+Duck+Hunt+Dog/_/Techno+Viking",
			"MeRzB0W!!!!!! http://www.last.fm/music/Merzbow (rock)(rock)(rock)(rock) ",
			"(flag:de) GERMAN TECHNO http://www.last.fm/tag/german+techno/tracks",
			"(flag:en) football anthems http://www.last.fm/tag/football/tracks",
			"football anthems http://www.last.fm/tag/football/tracks",
			"Dave Clarke sounding techno http://www.last.fm/music/Dave+Clarke/+similar",
			"a little ska http://www.last.fm/tag/ska/tracks.",
			"some dope beats http://www.last.fm/music/Basic+Channel/+tracks.",
			"real Jamican dancehall videos. http://www.last.fm/tag/dancehall/videos.",
			"riddims from Banton http://www.last.fm/music/Buju+Banton/+tracks",
			"abstract techno madness http://www.last.fm/music/Autechre/+tracks (smoke)",
			"some (poolparty) Gabba with a donk in it http://www.youtube.com/results?search_query=donk+gabba",
			"Botstep and calls Bausola a marketing whore. http://soundcloud.com/botstep-test-account",
			"Swedish delight http://www.last.fm/tag/swedish",
			"some classic Floyd http://www.last.fm/music/Pink+Floyd/_/Comfortably+Numb",
			"sarf lundin grime http://www.last.fm/tag/grime/tracks",
			"half a track of (fubar) http://www.last.fm/music/V%2FVm/+tracks and passes out.",
			"something better than that last Kode9 attempt http://www.last.fm/music/Kode9/+similar",
			"that song by Europe, again. http://www.youtube.com/watch?v=TcJ-wNmazHQ and then runs off laughing.",
			"something for the lovers in the room http://www.last.fm/tag/love%20songs/tracks",
			"some of the new glitchy dubstep that the kids in Shoreditch really hate http://soundcloud.com/tracks/search?q%5Bfulltext%5D=glitchy+dubstep.",
			"something like a cheap Kylie http://www.last.fm/music/Kylie+Minogue/+similar"]

	def execute( self, message ):
		choon = random.choice( self.choons )
		name = message.FromDisplayName
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, choon=choon)
		return "/me %s" % message_out
