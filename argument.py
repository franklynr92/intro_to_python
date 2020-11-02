def greetMe(str):
    #This function greets the name passed in
    print("Welcome to the funciton", str)
    return

def calculateBattingAverage(atBats, hits, walks):
    #This function claculates batting average
    battingAverage = hits/(atBats-walks)
    print(battingAverage)
    return

#Function Calls
greetMe("Kevin")
#greetMe() causes error because missing argument
calculateBattingAverage(200,54,12)
calculateBattingAverage(300,108,6)
