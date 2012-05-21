import tweepy
import os

class TwitterConnector( object ):
	
	def __init__( self, creds_path ):

		fh = open( os.path.join( creds_path, 'consumer_token' ), 'r' )
		consumer_key, consumer_secret = fh.read().split(",")
		fh.close()

		fh = open( os.path.join( 'access_token' ), 'r' )
		key, secret = fh.read().split(",")
		fh.close()

		auth = tweepy.OAuthHandler( consumer_key, consumer_secret )
		auth.set_access_token( key, secret )
		self.api = tweepy.API( auth )

		self.name = self.api.me().screen_name

	def tweet( self, message ):
		if message.startswith( "/me" ):
			message = message[3:]
			message = message.lstrip()
		self.api.update_status( message )