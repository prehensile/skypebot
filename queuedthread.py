import Queue
import threading

class QueuedThread( threading.Thread ):

    def __init__(self):
        self._queue = Queue.Queue()
        self._abortflag = False

    def stop( self ):
        self._abortflag = True

    @property
    def is_running( self ):
        return !self._abortflag

    @property
    def queue(self):
        return self._queue

    def put_message( self, message ):
        self._queue.put( message )

    def pop_message( self ):
        message = None
        try:
            message = queue.get( False )
        except Queue.Empty:
            pass
        return message
