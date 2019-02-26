# Python assignment Question 10
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

# Approach:
# 1)    Import a plotting library, such as plotpy or matplotlib (Note: plotpy seems to require registration to use fully)
# 2)    Import numpy to give a greater range of functionality for number functions
# 3)    Plot all 3 functions using matplotlib
# 4)    Input labels, axis information, legend, and title

import matplotlib.pyplot as plt                                 # Import matplotlib
import numpy as np                                              # Import numpy

Number = np.arange(0.0,5.0,1.0)                                 # Set numbers in the range 0 to 5 in increments of 1 
                                                                # (Note that 5 is the upper bound and is not included in the calcs)

plt.plot(Number, Number, '-r', label='f(x) = x')                # 1st function f(x) = x, plotted with red line, and label
plt.plot(Number, Number**2, '-b', label='f(x) = x^2')           # 2nd function f(x) = x^2, plotted with blue line, and label
plt.plot(Number, 2*Number, '-g',label='f(x) = 2x')              # 3rd function f(x) = 2x, plotted with green line, and label
plt.legend(loc='upper left')                                    # Set location of plot legend to upper left hand corner
plt.axis([0,5,0,18])                                            # Set axis values, x: 0 to 5; y: 0 to 18 (the upper bounds are larger than the expected returns of the functions)
plt.xlabel('X values')                                          # Set x axis label
plt.ylabel('y values')                                          # Set y axis label
plt.grid(b=None, which='major', axis='both')                    # Show major lines for both axis
plt.title('Q.10 - Plot functions in Python', fontdict=None, loc='center', pad=None,)    # Show a title, with standard font, in a central location, and no padding
plt.show()                                                      # Show the plot of all of the above

# End program