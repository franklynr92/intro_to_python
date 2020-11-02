def employeeInformation(name="", ssn="000-000-000", position=""):
    print("Name:", name)
    print("Ssn:", ssn)
    print("Position:", position)
    return

def moreEmployee(name, *other):
    print("Employee Info:")
    print("Name:", name)
    for var in other:
        print(var)
    return

employeeInformation(name="Franklyn", ssn="000-000-000", position="CEO")
moreEmployee("Mark Lassoff", "Founder", "9-1-2009")
