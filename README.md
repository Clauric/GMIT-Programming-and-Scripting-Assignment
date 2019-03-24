# GMIT-Programming-and-Scripting-Assignment

## Table of Contents
  * [Introduction](#Introduction)
  * [Technologies and Libraries](#Technologies-and-Libraries)
  * [Setup](#Setup)
  * [Research](#Research)
  * [Questions Asked](#Questions-Asked)
  * [Sample of code and explanation](#Sample-of-code-and-explanation)
  * [Status](#Status)
  * [Other Information](#Other-Information)
  
  ## Introduction
  This ReadMe, and the associated scripts within this repository, were written for an assignment for a module in Programming and Scripting, as part of a Higher Diploma in Science (Data Analytics). The specific questions associated with each individual script are listed in the [Questions Asked](#Questions-Asked) section below. All scripts in this depository are named with the corresponding question at the start of their name. Specific thoughts on the approach for each solution is provided in the comments section at the start of each script. Additionally, a sample of code has been provided below, whit a walkthrough to illustrate how the codes are generally written.
  
  ## Technologies and Libraries
  ### Main Platform
  * Python 3.7.2
    
  ### Internal Libraries
  These libraries are native to Python and should not need to be installed in order to run the scripts. The questions that the libraries are needed for is listed after the library name.
  * Datetime - Q. 2, 8
  * Math - Q. 7 
  * Os - Q. 9
  * Random - Q. 9
  * String - Q. 6
  * Sys - Q. 9
  * Time - Q. 9
  
  ### External libraries
  These are libraries that are not normally part of the standard installation with Python, and will need to be installed prior to running some of these scripts. The questions that the libraries are needed for is listed after the library name.
  * Matplotlib.pyplot - Q. 10
  * NumPy - Q. 10
  
  ## Setup
  
  In order to run the scripts in this repository, it is necessary to have a complier capable of compiling Python 3.7.2. In addition, it will be necessary to install the external libraries described above if there is a requirement to run Q10.
  
  All the codes in this repository have been tested using <a href="https://cmder.net/">Cmder</a>, with the <a href="https://www.anaconda.com/">Anaconda</a> being the default Python platform.  
  
  ## Research
  Two separate types of research were carried out in order to solve the problems posed. These were:
  
  * Problem solving research
  * Code formatting research
    
  ### Problem solving research
  All research with regards to problem solving was treated as a thought exercise. As such, all problems, solutions, processes, and code logic was created from the author's own mind. The exception to this was the application of logic (Q.7, lines 103 & 104) for the Newton-Raphson method, which were sourced from various sites including:
  
  1. <a href="https://medium.com/code-zen/newtons-square-root-d8be94ec641e">Joe Chasinga's Medium post</a>
  2. <a href="http://www.sosmath.com/calculus/diff/der07/der07.html">Newton-Raphson Method</a>
 
  As the problems are fairly common problems, in terms of processes, and logic, there may be some overlap between the logic shown in the author's solutions, and existing information available on the web.
  
  ### Code formatting research
  This research involved identifying how to write a particular code sequence, in order to implement the solution that was implemented. The following sources were used for code research:
  
  * <a href="https://www.w3schools.com/python/default.asp">W3Schools</a>
  * <a href="https://docs.python.org/3.7/library/index.html">Official Python 3.7.2 documentation</a>
  * <a href="https://matplotlib.org/contents.html">Matplotlib</a>
  * <a href="https://docs.scipy.org/doc">NumPy</a>

 For Question 6 (the 2nd word problem), two additional sources were used as the basis of the solution. These were:
  * <a href="https://stackoverflow.com/a/17645629/4430536">user2357112's answer from StackOverflow</a>
  * <a href="https://www.dotnetperls.com/punctuation-python">Sam Allen's Instance Search page</a>
 
  ## Questions Asked
  The following questions were asked, and answered, in the Python scripts in this repository:
  
  1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
  2. Write a program that outputs whether or not today is a day that begins with the letter T.
  3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
  4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
  5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
  6. Write a program that takes a user input string and outputs every second word.
  7. Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.
  8. Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.
  9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.
  10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].
  
  ## Sample of code and explanation
  A sample code has been provided below. The example is used to demonstrate how the overall code is written, as well as some approaches to the solving of the questions. All the code, where practical, has been commented, to allow the reader to understand what is happening in each line. Where there is no comment, the line is viewed as being self-explanatory (i.e. else, if, while) or it has been explained in the previous line.
  
  The sample code provided is from Q.5, which deals with identifying if a number is prime.
  ```
  aFactor = 2                                                                 # Initial factor to be used
  bPrime = 1                                                                  # Sets prime check to 1 (e.g. prime)
  cResult = 1                                                                 # Result of number divided by the factor
  ```
 
 In the above code, the initial factor (aFactor) to be checked is 2, as 1 is a factor of all positive and negative whole numbers. bPrime is the key that changes from 1 (prime) to 0 (not a prime) based on the calculations. bPrime is set to 1 on the assumption that all numbers are prime (bPrime could equally be set to 0 based on the fact that there are more non-prime numbers than prime numbers). cResult is the result of the inputted number divided by the factor (aFactor).

```
  while aFactor >= cResult:                                                   # While the factor being checked is greater than the result
```

The code runs while aFactor is greater than the cResult. This is due to the <a href="https://www.khanacademy.org/math/pre-algebra/pre-algebra-arith-prop/pre-algebra-arithmetic-properties/v/commutative-law-of-multiplication">commutative properties</a> of multiplicands. This helps reduce the number of attempts the code needs to complete.

The code calls out a number of specific cases, in order to increase the scripts speed.

```
      if Number == 2 or Number == 3 or Number == 5:                           # 2, 3, and 5 are the initial 3 prime numbers
          bPrime = 1                                                          # Sets the prime check to 1 (e.g. prime)
          break
```

When the code runs through the while loop to check for a prime, the first check will be to determine if the inputted number is 2, 3, or 5, which are the first 3 prime numbers. If this is the case, the code will break out of the while loop, and return that the inputted value is a prime.

```
      elif (Number % 2 == 0) or (Number % 5 == 0) or (Number % 3 == 0):       # If number is even, ends in 5 or 3, or dividable by 3
          bPrime = 0                                                          # Sets the prime check to 0 (e.g. not a prime)
          break
```

A number is prime if its only whole number factors are 1 and itself. As such, it is possible to remove a large portion of calculations from the script if certain rules are followed. For example, any even number (except for 2) is not a prime, as it is divisible by 2. Likewise, if a number is divisible by 3 or by 5, they would also not be primes. It is possible quickly eliminate any number that is divisible by 2, 3, or 5, by using the modulo function of Python. This eliminates more than 77% of numbers from being checked by the slower iterative method of checking.

```
      else:
          cResult = Number / aFactor                                          # Calculation of cResult

          if cResult == int(cResult):                                         # Checks if the result is an integer
              bPrime = 0                                                      # Sets the prime check to 0 (e.g. not a prime)
              break

          else:
              aFactor += 1                                                    # Increases factor check by 1 if none of the previous conditions are met
 ```
 
 The final part of the code will check each possible whole number factor (aFactor), starting at 2 and incrementing in steps of 1, until it has determined that the result of the inputted number divided by the factor (cResult) is an integer, or the factor is greater than cResult. If cResult is an integer, it will set bPrime to 0 and break out of the while loop. 
 
 Each set of scripts is similarly written, with a combination of hardcoded rules, and while loops, to allow for flexibility and speed.
  
  ## Status
  The status of this project is complete. As there is a submission date of the 31st March, 2019, the files will be altered, from their current format, after that date. Where the last push/alter date is prior to the 31st March, 2019, that date can be viewed as the completion date.
  
  ## Other Information
  ### About the Author
  The author is a student of the Galway Mayo Institute of Technology, studying for a Higher Diploma in Science (Data Analytics). In addition, they work as a consultant in the financial services sector in Ireland, focusing on data migrations, and system replatforming for Irish and international financial institutions.
  
  ### Contact
  The author can be contacted using Clauricaune@gmail.com.
