import time
import datetime
now = time.time()
print("Now it is", time.asctime(time.localtime(now)))
print("Tomorrow it will be", time.asctime(time.localtime(now + (60*60*24))))
print("A year ago it was", time.asctime(time.localtime(now + (60*60*24*365))))
print("In 100 hours it will be", time.asctime(time.localtime(now + (60*60*100))))

birthday = datetime.datetime(1992, 8, 7, 8, 32, 33)

print("I was born on ", birthday.isoformat(' '))
