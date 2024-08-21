reading = open("note.txt", "r")
writing = open("new.txt", "w")

replacing =""

for x in reading:
    replacing = x
    if "old" in replacing:
        replacing.replace("old","new")
        print(replacing)
    writing.write(replacing)

writing.close()
writing = open("new.txt", "r")
print(writing.read())
writing.close()
reading.close()
