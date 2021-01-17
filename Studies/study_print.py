"""Link to the source https://youtu.be/k9TUPpGqYTo"""

LINER = '\n-----\n'
TEXT = "I am studying python that is taught by Corey in his video"
print(TEXT)
print(LINER + 'This is called slicing' + LINER)
print(TEXT[20])
print(LINER)
print(TEXT[20:30])
print(LINER)
print(TEXT[9:])
print(LINER + 'This is called Methods' + LINER)
print(TEXT.upper())
print(LINER)
print(TEXT.lower())
print(LINER)
print(TEXT.count("i"))
print(LINER)
print(TEXT.find('is'))
OLD = 'happy but never laugh'
NEW = OLD.replace('happy','sad')
print(NEW)
