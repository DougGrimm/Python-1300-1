'''Make a code that takes a height and velocity and uses thos values to find the maximum height 
and how long it takes to reach the ground'''

# Douglas Grimm
# 3/10/2023
# CSIS 1300-1

# the following code was retrieved from 
# https://stackoverflow.com/questions/55035431/what-is-the-reason-the-code-breaks-when-the-input-is-asked
# and will be changed and added to.

# create a method that requests the input of the height and velocity.
def getInput():
    print("")
    height = int(input("Enter the height of the object: "))
    velocity = int(input("Enter the velocity of the object: "))
    isValid(height,velocity)

# create another method that will take the input values and print the RESULT.
def isValid(height,velocity):
    if (height<=0):
        print("0 and negative numbers may not be used for the height")
    elif(velocity<=0):
        print("0 and negative numbers may not be used for the velocity")
    else:
        finalHeight = maxHeight(height,velocity)
        print("")
        print("Maximum height is", finalHeight, "feet")
        print("")
        airTime = ballTime(height,velocity)
        print("It will take about", airTime, "seconds before the object hits the ground")
        print("")
# this method will stop any non-positive integers and will take the final tested values and print them.
# maxHeight and ballTime are created to do the math for the height and velocity and send them back to
# this method.

# this method will put the height and velocity through the math to find the max height of the object.
def maxHeight(height,velocity):
    time = velocity/32
    maxH = height+(velocity*time)-(16*time*time)
    return maxH
# return maxH back to isValid

# this method takes the height and velocity through similar math and will count the seconds of air time 
# until the ballHeight reaches 0 or lower.
def ballTime(height,velocity):
    timeinAir = 0.1
    while(True):
        ballHeight = height+(velocity*timeinAir)-(16*timeinAir*timeinAir)
        if (ballHeight <= 0):
            break
        else:
            timeinAir += 0.1

    return timeinAir
# return timeinAir back to isValid

# this is where the code starts. It immediately calls the very first method at the top.
getInput()


# Thoughts
# the code is very easy to understand and gets the job done quite well. I did notice that 
# when putting in the "example output" values from the rubric that my "seconds before object hits ground"
# isn't 2.27 nor can it round to that so maybe the math isn't THAT precise.

