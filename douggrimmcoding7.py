'''Read a file and count the number of numbers as well as the min and max.'''

# Douglas Grimm
# 3/28/2023
# CSIS 1300


# https://stackoverflow.com/questions/47954216/python-count-numbers-from-input-file
# https://realpython.com/python-min-and-max/
# these sites were useful in helping me figure out some of the code to use in the process.



# this method opens the file and reads the list of numbers on it   
def testList():
    inFile = open("Numbers.txt", 'r') 
    testNumbers = [line.rstrip() for line in inFile] 
    return testNumbers

# this method uses the range function so as to not count too far. Also use the len function
# to find how many numbers are present in the file.
def countNum(finalNum):
    for count in range(len(finalNum)):
        count += 1 
    return count

# simply using the max function
def largeNum(finalNum):
    return max(finalNum)

# simply using the min function
def smallNum(finalNum):
    return min(finalNum)

# The main method where all of the other methods are called from
def main():
    finalNum = testList()
    print("There are",countNum(finalNum),"numbers in this file.", )
    print(largeNum(finalNum),"is the largest number.")
    print(smallNum(finalNum),"is the smallest number.")
main()