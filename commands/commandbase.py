class BaseCommand(object):
    
    def __init__( self ):
        self.tweets = True
        self.command_mappings = []
        self.enabled = True

    def generate( self, name ):
        return None

    def execute( self, message ):
        name = message.FromDisplayName
        return self.generate( name )

    def gift( self, recipient ):
        return self.generate( recipient )
        