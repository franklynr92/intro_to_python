poem = "With rue my heart is laden\n"
poem += "For golden friends I had\n"
poem += "For many a rose-lipped maiden\n"
poem += "And many a light foot lad\n"
poem += "By brooks too broad for leaping\n"
poem += "The light oot boys are laid\n"
poem += "The rose lipped girls are sleeping\n"
poem += "In fields where roses fade\n"
print(poem)
line = 1

##for letter in poem:
##    print("Line:", line, "Char: ", letter if letter.isupper() != True else "Line:", line, "Char: ", letter, "is Capital")
##    if(letter == "\n"):
##        line += 1
##        
##    if(letter.isupper() == True):
##        print("Line:", line, "Char: ", letter, "is Capital")
##    
char = 0
line = 1
while char < len(poem):
 if(poem[char] != '\n'):
     currentChar = poem[char]
     if(currentChar.isupper() == True):
         print("Line:", line, "Char:", char, currentChar, "Capital")
     else:
         print("Line:", line, "Char:", char, currentChar)
     char = char + 1
 else:
     line = line + 1
     char = char + 1
