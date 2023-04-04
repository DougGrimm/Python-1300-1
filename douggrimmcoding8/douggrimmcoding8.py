'''Create code that grabs states with capitals that start with the same letter and another code that
will take a state input and give back the information on it'''

# Douglas Grimm
# CSIS 1300
# 4/4/2023

# This code was pulled from the book and will be explained in detail.
# In order to get both programs into one file I placed them both in methods.
def firstPart():
   #open file
    inFile = open("StatesANC.txt", 'r', encoding="utf8")
    for line in inFile:
        data = line.split (",")
        letter = data[0][0:1]
        if data[3].startswith(letter):
            print((data[3].rstrip()) + ",", data[0])
    inFile.close()


def secondPart():
## Display data about a requested state.
    state = input("Enter the name of a state: ")
    infile = open("StatesANC.txt", 'r', encoding="utf8")
    found = False
    state_data = infile.readline()
    while (found == False) and (state_data != ""):
        data = state_data.split(",")
        if data[0] == state:
            print("Abbreviation:", data[1])
            print("Nickname:", data[2])
            print("Capital:", data[3].rstrip())
            found = True
        state_data = infile.readline()
    infile.close()

# this calls the methods in order for them to work 
firstPart()
secondPart()

# Creative Element
# I rearranged the txt file so that it was no longer in alphabetical order and then created a code
# that puts it back in order. 
with open("StatesANC.txt", 'r', encoding="utf8") as r:
    for line in sorted(r):
        print(line, end='')

# Thoughts
# Using the sort function turned out to be successful
# After placing the files into a folder to submit, I tried running the code again and now it won't work.
#






