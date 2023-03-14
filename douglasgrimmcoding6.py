'''Make a code that can recognize a word that has three consecutive alphabetical letters'''

# Douglas Grimm
# 3/13/2023
# CSIS 1300

def checkConsecutive(checkWord):
    length = len(checkWord)
    three = 3
    if length < three:
        print("String is too short for consecutive letters.")
    for i in range(length-2):
# ord converts a character to its integer equivalent and subtracts incrementing or decrementing values 
# to see if the letters are consecutive.
        if ord(checkWord[i]) == ord(checkWord[i+1])+1 == ord(checkWord[i+2])+2 or \
        ord(checkWord[i]) == ord(checkWord[i+1])-1 == ord(checkWord[i+2])-2:
            return checkWord[i:i+3] 
    return ""

# user will be asked to input a word with or without consecutive alphabetical letters.
# capitalization is important here otherwise it will flag it as "no consecutive letters."
inputWord = input("Enter a word to check (capitalization matters!): ") 
result = checkConsecutive(inputWord)

# this if statement does one last check to see if there are 3 consecutive letters and if not will
# procede to the else statement.
if len(result) == 3:
    print(inputWord, "has three consecutive alphabetical letters ", result, ".")

else:
    print(inputWord, "does not have any consecutive alphabetical letters.")


     
        
            