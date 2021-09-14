""" pcost.py
"""

################################################################################
# Exercise 1.27
# Now that you know how to read a file, let’s write a program to perform a
# simple calculation.

# The columns in portfolio.csv correspond to the stock name, number of shares,
# and purchase price of a single stock holding. Write a program called
# pcost.py that opens this file, reads all lines, and calculates how much it
# cost to purchase all of the shares in the portfolio.

# Hint: to convert a string to an integer, use int(s). To convert a string to
# a floating point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15
#------------------------------------------------------------------------------

# import os.path


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# with open(FILE_PATH, 'r') as fi:
#     headers = fi.readline()
#     data = fi.readlines()

# total_sum = sum((
#     float(line.strip().split(',')[1]) * float(line.strip().split(',')[2])
#     for line in data
# ))

# print("Total cost:", total_sum)


################################################################################
# Exercise 1.28: Other kinds of “files”
# What if you wanted to read a non-text file such as a gzip-compressed
# datafile? The builtin open() function won’t help you here, but Python has a
# library module gzip that can read gzip compressed files.

# Note: Including the file mode of 'rt' is critical here. If you forget that,
# you’ll get byte strings instead of normal text strings.
#------------------------------------------------------------------------------

import os.path
import gzip


BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
FILE_PATH = BASE + 'Data/portfolio.csv'
ZIPFILE_PATH = BASE + 'Data/portfolio.csv.gz'

with open(FILE_PATH, 'r') as fi:
    headers = fi.readline()
    data = fi.readlines()

total_sum = sum((
    float(line.strip().split(',')[1]) * float(line.strip().split(',')[2])
    for line in data
))

print("\nTotal cost:", total_sum)

print()
with gzip.open(ZIPFILE_PATH, 'rt') as fi:
    for line in fi:
        print(line, end='')


################################################################################
