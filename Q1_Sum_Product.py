# Python assignment Question 1:
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

# Thoughts:
# 2 possible options:

# Option 1 - use the iterative formula 'f(n) = 1 + 2 + ... + (n-1) + n' to calculate the sum of all integers less than and equal to n
#   i.e. if input = 4 then sum would f(n) = 1 + 2 + 3 + 4 -> f(n) = 10
#   Cons:   Requires each new value to be added to f(n) until n value had been reached.
#           For large values, this could take a long time.
#   Pros:   Demonstrates knowledge of iteration in formulae in Python

# Option 2 - use the formula 'f(n) = ((n+1) * n) / 2' to calculate the sum of all integers less than and equal to n
#   i.e. if input = 4 then sum would equal f(n) = ((4 + 1) * 4) / 2 -> f(n) = 10
#   Cons:   Does not demonstrate knowledge of iteration in formulae in Python
#   Pros:   Reduces number of calculations required, and speeds up process for vary large values.

# Decision:
# Choose Option 2, as code is shorter, more simplistic, relies on proven formulae, and faster for large values of n.

Number = int(input("Please input a whole positive number  "))       # Request input value from user, and converts from string to integer

while Number < 1:                                                   # While statement to catch if inputted value is invalid (i.e. less than 1)
    Number = int(input("Please input a WHOLE POSITIVE number  "))   # Request new value from user, and converts from string to integer

else:                                                               # Else if number is valid
    Sum = ((Number + 1) * Number) / 2                               # Performs calculation using formula f(n) = ((n + 1) * n) / 2
    print("Number entered: ",Number)                                # Prints number entered by user
    print("Sum of all digits less than and equal ", Number, " is: ", int(Sum))  # Prints result

# End of program