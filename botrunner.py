import Queue
from hookserver import HookServerMessage, HookServerThread
import skypebot
from messages import housekeeping
import subprocess
import logging
import time

# set up logging
logging.basicConfig( filename="skypebot.log", level=logging.INFO, filemode='w' )
#logging.captureWarnings( True )
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

 # set up http server to listen for github pushes
logging.info( "Staring up github HookServer..." )
retries = 3
hook_server = None
while retries > 0:  
    try:
        hook_server = HookServerThread()
    except Exception:
        pass
    retries -=1
    if hook_server is None:
        wait( 10 )
    else:
        break
if hook_server is None:
    sys.exit()
hook_server.start()

# run bot
try:
    hookserver_message = None
    run_outer = True
    while run_outer:
        logging.info( "Entering outer runloop, starting bot thread..." )
        # init & start new bot thread
        bot_thread = skypebot.BotThread()
    	bot_thread.start()
        run_inner = True
        logging.info( "Entering inner runloop..." )
    	while( run_inner ):
            hookserver_message = hook_server.pop_message()
            if hookserver_message is not None:        
                # recieved a push notification from github
                if hookserver_message.code == HookServerMessage.RECIEVED_PUSH:
                    logging.info( "Recieved push notification..." )
                    # construct quit messge for bot
                    commits = hookserver_message.payload[ 'commits' ]
                    commit_author = commits[0]['author']['name']
                    message_out = housekeeping.update_message_for_name( commit_author )
                    bot_thread.stop( message_out )
                    bot_thread = None
                    # drop to outer loop; restart bot_thread
                    run_inner = False
                    # update from git repo
                    subprocess.call( [ "git", "pull" ] )
                    # reload skypebot module
                    skypebot = reload( skypebot )
            time.sleep( 1 )

except KeyboardInterrupt:
    logging.info( "KeyboardInterrupt!" )

# shut down threads cleanly
if bot_thread.is_running:
    logging.info( "Shutdown bot thread..." )
    bot_thread.stop()
logging.info( "Shutdown hook server..." )
hook_server.stop()

logging.shutdown()
