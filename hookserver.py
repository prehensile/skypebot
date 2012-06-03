import SocketServer
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import queuedthread
import cgi
import json
import logging

class HookRequestHandler( BaseHTTPRequestHandler ):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        return

    def do_POST(self):
        
        fields = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                    })

        payload_in = fields['payload'].value
        print payload_in
        payload = None
        try:
            payload = json.loads( payload_in )
        except Exception:
            pass
        self.server.payload = payload

        self.send_response(200)
        self.end_headers()

class HookServerMessage( object ):
    RECIEVED_PUSH = 0
    def __init__(  self, code, payload ):
        self.code = code
        self.payload = payload

class HookHTTPServer( SocketServer.TCPServer ):
    @property
    def payload(self):
        return self._payload
    @payload.setter
    def payload(self, value):
        self._payload = value

    def __init__( self ):
        SocketServer.TCPServer.__init__( self, ("", 31337), HookRequestHandler )

    def handle_request( self ):
        self._payload = None
        SocketServer.TCPServer.handle_request( self )
    

class HookServerThread( queuedthread.QueuedThread ):

    def stop( self ):
        if self.httpd:
            self.httpd.timeout = 1
        super(HookServerThread,self).stop()

    def run( self ):
        self._abortflag = False
        self.httpd = HookHTTPServer()
        self.httpd.timeout = 5
        
        while not self._abortflag:
            try:
                self.httpd.handle_request()
            except Exception, e:
                logging.info( e )
                pass

            if self.httpd.payload is not None:
                message = HookServerMessage( HookServerMessage.RECIEVED_PUSH, self.httpd.payload )
                self.put_message( message )
        
        self.httpd.socket.close()