'''Make a code that displys the team that won more than 4 times and counts up all the wins of every team'''

# Douglas Grimm
# CSIS 1300
# 4/5/2023

import collections

# open file
with open("Rosebowl.txt", 'r', encoding = "utf8") as f:
   
    # count each individual line and add duplicates
    c = collections.Counter(f.readlines())

    # uses c.most_common to count all instances of a team and if it equals 4 or higher it displays them
    print("Won 4 games or more: ")
    for k, v in c.most_common():  
        if(v >= 4):
            print(k)
   
    # sorts the data by "most common" giving it a descending order
    print("Leaderboards: ")    
    for k, v in c.most_common():
        print(k, v)

f.close()

# Thoughts
# Same issue with the code not working once being thrown into a folder. Says it cannot find
# the txt file.