gpas = (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)
#gpas[1] = 2.25
x = 0
total = 0
for g in gpas:
    total = total + gpas[x]
    x += 1

average = total/len(gpas)
print("The average GPA is: ", average)

studentGpas = {"Bob" : 3.14,
               "Mark" : 3.45,
               "Melissa" : 3.98,
               "Travis" : 2.55,
               "DeeDee" : 3.24,
               "Ian" : 2.27}

x2 = 0
total2 = 0
for k,v in studentGpas.items():
        total2 = total2 + v

     

average2 = total2/len(studentGpas)
highest = max(studentGpas.values())
lowest = min(studentGpas.values())

print("The average GPA is: ", average2)
print("The hihgest GPA is: ", highest)
print("The lowest GPA is: ", lowest)

