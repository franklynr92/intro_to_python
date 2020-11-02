import time

localtime = time.localtime(time.time())
print(localtime)

formattedtime = time.asctime(time.localtime(time.time()))

print(formattedtime)
