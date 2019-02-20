# Python assignment Question 7
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# Thoughts:
# The easiest way to do this program would be to call the math.sqrt() function from Python. 
# In addition, there are numerous possible ways of approaching this problem from a more iterative perspective. 
# For coding the 2 main approaches seem to be either an over/under approach, or using the Newton-Raphson method.

# Over/under method:
# In this approach, an initial guess is taken (usually 1), and squared. The guess is then increased incrementally (by a set increment - usually 1), until the square of 
#   the guess is greater than the input value.
# The guess is then decreased in increments (usually 1/10 of the previous increment) and squared, until the squared value is less than the input value.
# The approach is then repeated (i.e. increased then decreased), in decreasing increments (usually 1/10 of the previous increment), until a desired level of accuracy is achieved.

# Issues:
# If the initial guess is far away from the square root, it can take time for the guess squared to surpass the initial input.
# Level of accuracy needs to be determined, as 1 decimal place would only require 2 iterations, while 10 decimal places would require more iterations, and therefore time.

# Newton-Raphson method:
# Also known as the Babylionian method or Heron's method.
# Iterative approach is based on the assertion that for an initial input of 'S', the value 'x' is an overestimation of the square root, while 'S/x' is an underestimation.
# Using the average of the 2 numbers, it is possible to reduce the values of 'x' and 'S/x' so that they converge at a sngle value.
# Programmatically this can be done by using the formula x1 = (x0 + (S/x0)) / 2 iteratively until the difference between x1 and x0 is less than a certain value
# This method is the method that is on the board of the Non-Linear equations class in the movie 21 (starting at 13:21).

# Issues:
# This method has been know to have problems where the initial guess 'x' is too far from the actual square root of 'S'.

# Decision:
# Attempt to program both methods, and show any difference between the estimated roots at 6 decimal places.
# The math.sqrt(), while a bit of a cheat, will also be used to highlight any diferences between the 3 methods, at 6 decimal places.

# Note: 
# Using large values, especially values greater than 1 million will slow, if not crash python.
# This is due to the fact that the incrementations are in steps of 1.

import math                                                                 # Imports the python maths function into the program

while True:
    try:
        Number = float(input("Please input a positive number  "))           # Request input value from user, and converts from string to float

    except ValueError:                                                      # Error/exception handling for float entries
        print("Sorry, I did not understand that entry")                 
        continue

    if Number <= 0:                                                         # Check if number positive, as the square root of a negative number i an imaginary number (represented by i)
        print("Sorry, that number is not positive")
        continue

    else:
        break

# Start value
# Decide the start value based on the Number
      
if Number < 10000:                                                          # When input is less than 10,000
    bStart = 1                                                              # Start value is 1
    zStart = 1                                                              # Start value is 1 (x0)

elif Number < 1000000:                                                      # When input is less than 1,000,000
    bStart = 100                                                            # Start value is 100 (100 x 100 = 10,000)
    zStart = 100                                                            # Start value is 100 (100 x 100 = 10,000)

elif Number < 100000000:                                                    # When input is less than 100,000,000
    bStart = 1000                                                           # Start value is 1,000 (1,000 x 1,000 = 1,000,000)
    zStart = 1000                                                           # Start value is 1,000 (1,000 x 1,000 = 1,000,000)

else:                                                                       # When input is greather than 100,000,000
    bStart = 10000                                                          # Start value is 10,000 (10,000 x 10,000 = 100,000,000)
    zStart = 10000                                                          # Start value is 10,000 (10,000 x 10,000 = 100,000,000)

 # Over/under method   

aCount = 0                                                                  # Iteration count
cDivisor = 1                                                                # Divisor used to get more accurate values
dSquare = 0                                                                 # Square of estimate values

while aCount <=8:                                                           # While iteration count is less than equal to 8 (this will result in an answer to 7 decimal places)
    dSquare = bStart ** 2                                                   # Setting value to the square of the guess value

    if (aCount % 2) == 0:                                                   # If the iteration count is even
        while dSquare < Number:                                             # While dSquare is less than the input number
          bStart = bStart + (1 / cDivisor)                                  # The start value is incremented by 1 + cDivisor, which increments in values of 10
          dSquare = bStart ** 2                                             # Setting the new value to the square of the ttart value

    else:                                                                   # If the iteration count is odd
        while dSquare > Number:                                             # While dSquare is less than the input number
            bStart = bStart - (1 / cDivisor)                                # The start value is incremented by 1 + cDivisor, which increments in values of 10
            dSquare = bStart ** 2                                           # Setting the new value to the square of the ttart value
    
    aCount += 1                                                             # aCount iterates by 1
    cDivisor = cDivisor * 10                                                # cDivisor is multiplied by 10 (i.e. 1, 10, 100, etc. - this will decrease the iteration by 1/10th for each pass)

# Newton-Raphson method

yNewNum = 0                                                                 # New value of estimate (x1)
xRoot = 0                                                                   # Used to transfer values between yNewNum and zStart

while abs(zStart - yNewNum) > 0.0000001:                                    # While the difference between zStart and yNewNum is greater than 0.0000001 (7 decimal places)
    yNewNum = (zStart + (Number / zStart)) / 2                              # x1 = (x0 + (S/x0)) / 2 
    zStart = yNewNum                                                        # Replace the value x0 with the value of x1
    yNewNum = xRoot                                                         # Replace the value of x1 with the transfer value
    xRoot = zStart                                                          # Replace the transfer value with x0

# Final print outs

print("Start number is:         ", Number)                                  # Print the number that was entered
print("Square roots are:")                                                  # Prints the line "square roots are:"
print("Math.SQRT() =            ", round(float(math.sqrt(Number)),6))       # Prints the value using the math.SQRT function
print("Over/under method =      ", round(float(bStart),6))                  # Prints the results using over/under method
print("Newton-Raphson method =  ", round(float(zStart),6))                  # Prints the results using Newton-Raphson method

# End of program
