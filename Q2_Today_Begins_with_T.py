# Python assignment Question 2
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.

# Approach:
# 1)    Get today's date using the datetime.datetime function 
# 2)    Get the name of today's date using the strftime functionality as part of datetime.datetime
# 3)    Set the value of today's date to a string
# 3)    Check the first letter of the string to determine if it begins with "T"
# 4)    Print the results.

import datetime                                                 # Import the date time function

Today = datetime.datetime.today()                               # Set Today string to today's name
Today_name = Today.strftime("%A")

if Today_name[0] == "T":                                        # If the first character (Python starts at character 0) of the name begins with "T"
    print("Yes - today begins with a T.")                       # Print "Yes - today begins with a T."

else:                                                           # If the first character (Python starts at character 0) of the name does not begin with "T"
  print("Boo - today does not begin with a T.")                 # Print "Boo - today does not begin with T."

# End of program