import random

x = 0
y = 0
while x < 100:
    number = random.randrange(1,10)
    y = y + number
    print(number)
    x=x+1


    
print("the sum is:",y)
print("the average is:",y/100)
