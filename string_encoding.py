# File: string_encoding.py
# Description: Encoding string by grouping repeated letters with itertool library
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Encoding string by grouping repeated letters with itertool library // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/String_Encoding_with_Itertools (date of access: XX.XX.XXXX)



# Implementing the task
# Encoding input string
# Finding all repeated letters and calculating them
# Returning encoded string with number + letter
# No number for letters that are met only once
# Example
# input string: aaaBBBBBaCCCCcFfff
# Encoded string: 3a5Ba4CcF3f
# This task is so called basic compressing task

# Importing library to group the same letters in the string
import itertools


# Creating function for encoding
def encode(input_string):
    # Going through the input string and returning encoded string
    for letter, same in itertools.groupby(input_string):
        # Calculating number of repetitions
        number = sum(1 for _ in same)
        # Returning just letter if it's alone and number+letter if it's not alone
        # Returning a generator by using 'yield'
        yield letter if number == 1 else str(number) + letter


# Input string
# Implementing function
# Joining results from function in one string
# Showing the result
# Everything in one line
print(''.join(encode(input())))
