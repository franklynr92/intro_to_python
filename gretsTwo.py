def greetTwoPeople(person1, person2):
    #this funciton greets two people
    print("Greetings", person1)
    print("Hellow, How are you?", person2)
    return

greetTwoPeople(person2="Brett",person1="Mark")


def calculateBa(atBats, hits, walks):
    ba = hits/(atBats-walks)
    print(ba)
    return

calculateBa(atBats=317, walks=25, hits=67) 
