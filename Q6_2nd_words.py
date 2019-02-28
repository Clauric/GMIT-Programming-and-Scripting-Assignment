# Python assignment Question 6
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that takes a user input string and outputs every second word.

# This solution is based heavily on user2357112's answer on stackoverflow (https://stackoverflow.com/a/17645629/4430536) 
# and Sam Allen's page at https://www.dotnetperls.com/punctuation-python

# Approach:
# 1)    Get the to input a sentence.
# 2)    Pass the input to a function to strip out punctuation (Note: it can be done without passing to a function, but it allows for greater uniformity of the process)
# 3)    Pass the output of the function to the original code.
# 4)    Split the sentence into individual words, using the split command.
# 5)    Print out the sentence generated. 

# Note:
# As long as there is an input, there will be an output, even if it blank.
# If there is 1 or one word in the input, there will be no output. If there is at least one space and 2 distinct alphanumeric entries, there will be a non-blank output.

import string                                           # Import string

def f_remove_punctuation(value):                        # Created definition to remove puncuation
    
    new_output = ""                                     # New output is blank
    
    aCount = 0                                          # Iterative count starting at 0

    while aCount < (len(value)):                        # While loop until iterative count is less than the length of the value
        if value[aCount] not in string.punctuation:     # Check if the character value is not in the list of punctuations
            new_output += value[aCount]                 # Add the character to the output value
            aCount += 1                                 # Increment count by 1
        
        else:                                           # If the character is in the punctuation list
            aCount += 1                                 # Increment by 1 (i.e. skip the character)
    
    return new_output                                   # Returns the output from the function

sentence = input("Please enter a sentence:")            # Request input value from user, and converts from string to integer

new_sentence = f_remove_punctuation(sentence)           # Pass the output of the function to the new_sentence variable.
                                                        # Note this line could be skipped, and the function could be passed directly into the line below instead of new_sentence.
                                                        # This was done to avoid complexity in the code.

second_word = ' '.join(new_sentence.split()[1::2])      # Splits the sentence inputted, based on the spaces in the sentence, and joins the words found after the 1st word,
                                                        # and every second word thereafter, with a space between the words

print()                                                 # Prints a blank line
print("Every second word of your input is:")            # Prints the line "Every second word of your input is:"
print()                                                 # Prints a blank line
print(repr(second_word))                                # Prints the variable second_word as deterined by line 5

# End program
