# Python assignment Question 5:
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

# Thoughts
# A prime is a positive whole number, greater than 1, that has, as its factors, 1 and itself.
# Therefore:
# 1) By rule, neither 0 nor 1 can be primes (0 has not factors, 1 only has itself as a factor).
# 2) Any even number greater than 2 cannot be a prime, as it is divisible by 2.
# 3) Any number greater than 5, that ends in either 5 or 0, cannot be a prime, as it is divisble by 5.

# Additionally
# In order to factors, the input number divided by the factor being tested, must result in a whole number (i.e. 21 / 6 = 3.5 which is not a positive whole number)
# Due to the rules of multiplication, it is only necessary to test the factors until the test factor is greater than the result 
#   (e.g. if input number is 99, there is no need to go beyond 10 as a factor test as 99 / 10 = 9.9)

while True:
    try:
        Number = int(input("Please input a positive number  "))             # Request input value from user, and converts from string to float

    except ValueError:                                                      # Error/exception handling for float entries
        print("Sorry, I did not understand that entry")                 
        continue

    if Number <= 0:                                                         # Check if number positive, as the square root of a negative number i an imaginary number (represented by i)
        print("Sorry, that number is not positive")
        continue

    else:
        break

aFactor = 2
bPrime = 1
cResult = 1

while aFactor >= cResult:
    if Number == 2 or Number == 3 or Number == 5:                           # 2, 3, and 5 are the initial 3 prime numbers
        bPrime = 1
        break

    elif (Number % 2 == 0) or (Number % 5 == 0) or (Number % 3 == 0):
        bPrime = 0
        break
    
    else:
        cResult = Number / aFactor

        if cResult == int(cResult):
            bPrime = 0
            break
        
        else:
            aFactor += 1    

print()
print("Inputted number is: ", Number)

if bPrime == 0:
    print("Inputted number is:  NOT a PRIME")

else:
    print("Inputted number is:  PRIME")