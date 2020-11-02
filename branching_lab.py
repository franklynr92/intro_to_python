subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]

if subjectList[3] == "Geography":
    takingGeography = True

print (takingGeography)

average = (gpas[0] + gpas[1] + gpas[2])/len(gpas)

if average >= 3.33:
    print("average is 3.33 or greater")
else:
    print("Average is less than 3.33")


age = 17
print('Elgibible to buy alcohol' if age >= 18 else 'No drinking for you')

citizen = False
print('You may vote' if citizen == True else 'sorry no voting for you')
