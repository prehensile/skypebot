class BaseCommand(object):
    
    def generate( self, name ):
        return None

    def execute( self, message ):
        name = message.FromDisplayName
        return self.generate( name )

    def gift( self, recipient ):
        return self.generate( recipient )
        