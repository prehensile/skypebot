from commands import pondercommand
from commands import shoutoutcommand
from commands import bullshitcommand

# bullshit
test_command = bullshitcommand.BullshitCommand()
print test_command.generate( "prehensile" )

# ponder
test_command = pondercommand.PonderCommand()
print test_command.generate( "prehensile" )

# shoutout
test_command = shoutoutcommand.ShoutoutCommand()
test_message = { "Body": "#shoutout to the berlin massive" }
print test_command.execute( test_message )
