from string import Template
import random

update_messages = [
	Template( "/me goes glassy eyed for a moment as an update is recieved. If he doesn't come back it's $name's fault." ),
	Template( "/me runs from the bar, screaming something about $name and an update." )
]

new_chat_messages = [
	"/me re-appears a split nanosecond after his ratty carpet slippers do.",
	"/me rides in on a tiny tricyle."
]


def update_message_for_name( name ):
	template = random.choice( commit_messages )
	return template.substitute( name=name )

def new_chat_message():
	message = random.choice( new_chat_messages )
	return( message )
