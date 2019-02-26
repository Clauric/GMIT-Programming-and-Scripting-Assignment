# Python assignment Question 6
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that takes a user input string and outputs every second word.

sentence = input("Please enter a sentence:")       # Request input value from user, and converts from string to integer

aCount = 1

for word in sentence.split():
    if aCount % 2 == 1:
        aCount += 1
    
    else:
        aCount += 1
        print("\n".join(word for word in sentence))

# End program