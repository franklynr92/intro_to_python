bands = ["Journey", "Swizza", "Sefa", "MCR", "ABBA"]
websites = ["Yahoo!", "google", "myspace"]
print(bands)
print(bands[1:3])
bands[0] ="bitchnuggets"
print(bands)


computers = ("IBM", "HP", "MAC", "DELL", "Toshiba")
print(len(computers))

x=0
while x < len(computers):
    print(computers[x])
    x += 1

scores = (10500, 11000, 12000, 14000, 50000, 950)
print("min:", min(scores))
print("max:", max(scores))

websites = tuple(websites)
websites[0] = "Bing"
