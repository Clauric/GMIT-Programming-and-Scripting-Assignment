# Python assignment Question 9
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

# Approach:
# 1)    Ask user for location of a file they want read
# 2)    Check that the file exits at the location specified (i.e. check for a file with the same name, on the filepath specified)
# 3)    Open and read the file
# 4)    Print out every second row

# Additional items:
# Include a time pause to seem like the program is digesting the file
# Print out the row number that is being printed
# Include a pause between each print row, to allow the row to be read.

# Note:
# There is a time pause of 3/8ths of a second between each row. This means that for every 200 rows of a file, it takes about 38 seconds to print out the program.
# Therefore, it is not recommended to run this program for very large files, as it may take a long time to complete.

import sys
import os
import random
import time
 
while True:
    user_input = input("Enter the path of your file (Remember to include the file name and extension): ")       # Asks user for filepath of file to be used
    
    if not os.path.isfile(user_input):                                                                          # If filepath is not correct (e.g. missing or incorrect filename)
        print()                                                                                                 # Print a blank line
        print("I did not find the file at "+str(user_input))                                                    # Print that file was not found
        print()                                                                                                 # Print a blank line
        continue                                                                                                # Goes back to asking for a correct filepath
    
    else:                                                                                                       # If filepath is correct
        break                                                                                                   # Break out of while loop

iFile = open(user_input,'rt')                                                                                   # Opens file, if present, in read only mode ("r"), specifying that it is a text file ("t")

# added a pause step to see how it works
bTime= float(random.randrange(1,4)*2.5)                                                                         # Random number generator for values between 2.5 and 10

print()                                                                                                         # Print a blank line
print("I found your file. Please wait", bTime, "seconds while I digest it, and return every 2nd line")          # Reads file
time.sleep(bTime)

aCount = 1                                                                                                      # Count value

for line in iFile:                                                                                              # For all the lines in the file

    if aCount % 2 ==0:                                                                                          # If count is even
        print(aCount, line, end=' ')                                                                            # Prints aCount value and corresponding line from file
        aCount += 1                                                                                             # Increase count by 1
        time.sleep(0.375)                                                                                       # 3/8 second delay to allow for file output to be readable
    
    else:                                                                                                       # If count is uneven
        aCount += 1                                                                                             # Increase count by 1

# End program