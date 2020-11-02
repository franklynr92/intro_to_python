file = open("namesList.rtf", "a")
name=''
listOfNames = ""
while(name != "XXX"):
    name = input("Name: ")
    if (name != 'XXX'):
        listOfNames += ","
        listOfNames += name
print("Saving", listOfNames)
file.write(listOfNames)
file.close()
