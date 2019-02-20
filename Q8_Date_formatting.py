# Python assignment Question 8
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

# Approach:
# 1)    Get today's date using the datetime.datetime function 
# 2)    Get the name of today's date using the strftime functionality as part of datetime.datetime
# 3)    Get the suffix of the date (i.e. st, nd, rd, th) as specified in the question
# 4)    Print out the date using the format values available in Python

import datetime                                                 # Import the date time function

Today = datetime.datetime.today()                               # Set Today string to today's name
Today_day = Today.strftime("d")                                 # Set Today_day to the date in the month (e.g. 21)

if Today_day[-1] == 1 and Today_day != 11:                      # If the last digit of the date is 1 and it is not the 11th of the month
    Today_Qual = "st"                                           # Set the date suffix to "st"

elif Today_day[-1] == 2 and Today_day != 12:                    # If the last digit of the date is 2 and it is not the 12th of the month
    Today_Qual = "nd"                                           # Set the date suffix to "nd"

elif Today_day[-1] == 3 and Today_day != 13:                    # If the last digit of the date is 3 and it is not the 13th of the month
    Today_Qual = "rd"                                           # Set the date suffix to "rd"

else:                                                           # In all other cases
    Today_Qual = "th"                                           # Set the date suffix to "th"

print(Today.strftime("%A, %B %#d")+Today_Qual, Today.strftime("%Y"), "at", Today.strftime("%I:%M%p"))                       # Print the date in the format required

# Explanation of line 30:

# Today.strftime("%A, %B %#d")+Today_Qual - print out Today using the format:
# %A - Long version of day, followed by a comma (,)
# %B - Long version of month
# %#d - Date (from 01 - 31), without the leading zero (0) if required
# +Today_Qual - add the appropriate suffix without a space between the date and suffix

# Today.strftime("%Y") - continue printing out Today using the format:
# %Y - 4 digit version of the year
# at - Insert the word "at"

# Today.strftime("%I:%M%p") - continue printing out Today using the format:
# %I - Hours (from 00 - 12)
# %M - Minutes (from 00 - 59)
# %p - AM or PM

# End of program