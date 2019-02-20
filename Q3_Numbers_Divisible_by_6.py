# Python assignment Question 3:
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

# Thoughts:
# In order to identify a number that is divisible by 6, but not by 12, it is required that the number, when divided by 6 results in an uneven number.
# An example of the principle would be:
# 90 / 6 = 15, while 96 / 6 = 16 which is the same as 96 / (6 x 2) = (16 / 2)

# Steps
# Identify 1st number greater than 1,000 which, when divided by 6 results in an uneven number.
# While the numerator is less than 10,000, keep adding 12 to the initially identified number.

Number = 1000                                           # Start number as per assignment

while Number <= 1012:                                   # By rule, there must be a number that is divisible by 6 within the first 12 numbers
    if Number % 6 != 0:                                 # If number is not divisible by 6, increment by 1
        Number += 1
    
    elif Number % 12 == 0:                              # If number is not divisiblw by 12, increment by 1
        Number += 1
    
    else:                                               # If the number is divisblw by 6 but not by 12
        break                                           # Step out of loop

aCount = 1                                              # Iteration count

while Number < 10000:                                   # While the number is less than 10000, per assignment
    print("#", aCount, "value is: ", Number)            # Print the iteration number as well as the number that is divisible by 6 but not 12
    Number += 12                                        # Increase Number by
    aCount += 1                                         # Increase count by 1

# End program