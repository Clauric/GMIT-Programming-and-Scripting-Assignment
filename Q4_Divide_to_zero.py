# Python assignment Question 4:
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

# Approach:
# Get input value from user
# Check if value > 0, if not ask for another value
    # Introduce special case for value of 1
# Check if even, divide by 2.
# Check if odd, multiply by 3 then add 1 
    # (number before adding 1 will always be odd, as odd * odd = odd)
# repeat until input value = 1

# Thoughts:
# Process of divison of even numbers, to achieve the target of 1, would be faster if value is divisble by 4 (2^2) or 8 (2^4). This is not included in the calculation.

while True:
    try:
        Number = int(input("Please input a whole positive number  "))       # Request input value from user, and converts from string to integer

    except ValueError:                                                      # Error/exception handling for non-integer entries
        print("Sorry, I did not understand that entry")                 
        continue

    if Number < 1:                                                          # Check if number positive
        print("Sorry, that number is not positive")
        continue

    else:
        break

print("Start number is: ", Number)
        
if Number = 1:                                                              # Special case of input value = 1
    print("Input number is 1. There are no further calculations to be done")
    
Else:

    while Number > 1:                                                       # Repeat until the target value of 1 is reached

        VarNum = Number                                                     # Assign VarNum the input or calculated value

        if (VarNum % 2) == 0:                                               # Checks if number is even
            Number = int(VarNum / 2)                                        # Divides number by 2
            print("New value is: ", Number)                                 # Prints the new number value
        else:
            Number = int((VarNum * 3) + 1)                                  # Multiply number by 3 then add 1
            print("New value is: ", Number)                                 # Prints new number

# End of program