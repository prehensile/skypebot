import Skype4Py

skype = Skype4Py.Skype(Transport='x11')
skype.Attach()

chats = skype.Chats
for chat in chats:
    chat.Unbookmark()
    chat.Disband()
    chat.Leave()

api.ResetCache()