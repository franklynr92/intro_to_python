import random

names = ["Fred", "mary", "marrryy", "mee", "kevin", "June"]

print(random.choice(names))
print(random.randrange(1,1000,10))

random.shuffle(names)
print(names)
