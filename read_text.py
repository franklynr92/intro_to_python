employeeFile = open("employees.txt.rtf", "r")
#print (employeeFile.read(3))
#print (employeeFile.readline(3))

i = 1
for line in employeeFile:
    print(i,":", line)
    i = i + 1
