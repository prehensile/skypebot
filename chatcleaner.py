import Skype4Py

skype = Skype4Py.Skype(Transport='x11')
skype.Attach()

chats = skype.Chats
for chat in chats:
    try:
    	chat.Unbookmark()
    except Exception, e:
        pass
    try:
        chat.Disband()
    except Exception, e:
        pass    
    chat.Leave()

api.ResetCache()
