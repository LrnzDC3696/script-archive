"""Link for the source video https://youtu.be/daefaLgNkw0 """

words = {
    "book":"A thing where it has information ",
    "pen":"A tool to write or take notes of data",
    "pencil":["A pen but erasable","you can use an eraser"]
    }
    

print(words)
print()
print(words["book"])
print()
print(words.get("notebook")) #returns None if it does not exist
print(words.get("notes", "It does not exist")) #returns the second input if it does not exist
print(words.get("pen"))

print(len(words))
print(words.items())
print(words.values())
print(words.keys())