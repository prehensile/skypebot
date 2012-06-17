import twitterconnector
from messages import streetnoise
import logging

logging.basicConfig( filename="twitter_tester.log", level=logging.INFO, filemode='w' )
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

logging.info( "Starting up Twitter connector..." )
twitter_connector = twitterconnector.TwitterConnectorThread()
twitter_connector.creds_path = "twitter_creds"
twitter_connector.track_keywords = ["lndlrd"]
twitter_connector.start()

abortflag = False

while not abortflag:
    new_statuses = twitter_connector.pop_stream()
    for status_in in new_statuses:
        try:
            message_out = streetnoise.message_for_incoming_status( status_in )
            logging.info( message_out )
        except Exception, e:
            print( e )    
time.sleep(1)

