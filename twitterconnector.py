import tweepy
import os

class TwitterListener( tweepy.StreamListener ):

    @property
    def delegate( self ):
        return self._delegate
    @delegate.setter
    def delegate( self, value ):
        self._delegate = value

    def on_status(self, status):
        logging.info( "Status recieved: %s" % status )
        if self._delegate:
            self._delegate.push_status( status )

    def on_error(self, status_code):
        logging.info( "Tweepy stream error, status code = %s" % status_code )
        return True  # keep stream alive

    def on_timeout(self):
        logging.info( "Tweepy stream timeout" )
        pass


class TwitterConnector( object ):
    
    def __init__( self, creds_path, track_keywords=None ):

        self.api = None
        self.streaming_api = None
        self.stream_buffer = []
        error = None

        try:
            fh = open( os.path.join( creds_path, 'consumer_token' ), 'r' )
            consumer_key, consumer_secret = fh.read().split(",")
            fh.close()
        except IOError, e:
            error = e

        try: 
            fh = open( os.path.join( creds_path, 'access_token' ), 'r' )
            key, secret = fh.read().split(",")
            fh.close()
        except IOError, e:
            error = e

        if error is None:

            auth = tweepy.OAuthHandler( consumer_key, consumer_secret )
            auth.set_access_token( key, secret )
            self.api = tweepy.API( auth )

            if track_keywords is not None:
                logging.info( "Connecting Twitter stream for keywords %s" % track_keywords )
                listener = TwitterListener()
                listener.delegate = self
                self.streaming_api = tweepy.Stream( auth, listener, timeout=None )
                self.streaming_api.filter( track=track_keywords )

            self.name = self.api.me().screen_name

    def tweet( self, message ):
        if self.api:
            if message.startswith( "/me" ):
                message = message[3:]
                message = message.lstrip()
            self.api.update_status( message )

    ##
    # Streaming functions

    def push_status( self, status ):
        self.stream_buffer.append( status )

    def pop_stream( self ):
        out = self.stream_buffer
        self.stream_buffer = []
        return out

    def disconnect( self ):
        if self.streaming_api is not None:
            self.streaming_api.disconnect()
    
    
