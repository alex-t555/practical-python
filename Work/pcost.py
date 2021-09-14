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

# print("\nTotal cost:", total_sum)


################################################################################
# Exercise 1.28: Other kinds of “files”
# What if you wanted to read a non-text file such as a gzip-compressed
# datafile? The builtin open() function won’t help you here, but Python has a
# library module gzip that can read gzip compressed files.

# Note: Including the file mode of 'rt' is critical here. If you forget that,
# you’ll get byte strings instead of normal text strings.
#------------------------------------------------------------------------------

# import os.path
# import gzip


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'
# ZIPFILE_PATH = BASE + 'Data/portfolio.csv.gz'

# with open(FILE_PATH, 'r') as fi:
#     headers = fi.readline()
#     data = fi.readlines()

# total_sum = sum((
#     float(line.strip().split(',')[1]) * float(line.strip().split(',')[2])
#     for line in data
# ))

# print("\nTotal cost:", total_sum)

# print()
# with gzip.open(ZIPFILE_PATH, 'rt') as fi:
#     for line in fi:
#         print(line, end='')


################################################################################
# Exercise 1.30: Turning a script into a function
# Take the code you wrote for the pcost.py program in Exercise 1.27 and turn
# it into a function portfolio_cost(filename). This function takes a filename
# as input, reads the portfolio data in that file, and returns the total cost
# of the portfolio as a float.
#------------------------------------------------------------------------------

# import os.path


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# def portfolio_cost(file_name: str) -> float:
#     with open(file_name, 'rt') as fi:
#         _ = fi.readline()
#         data = fi.readlines()
#     return sum((
#             float(line.strip().split(',')[1])*float(line.strip().split(',')[2])
#             for line in data
#         ))

# total_cost = portfolio_cost(FILE_PATH)
# print('\nTotal cost:', total_cost)


################################################################################
# Exercise 1.31: Error handling
# What happens if you try your function on a file with some missing fields?

# >>> portfolio_cost('Data/missing.csv')
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "pcost.py", line 11, in portfolio_cost
#     nshares    = int(fields[1])
# ValueError: invalid literal for int() with base 10: ''
# >>>
# At this point, you’re faced with a decision. To make the program work you
# can either sanitize the original input file by eliminating bad lines or you
# can modify your code to handle the bad lines in some manner.

# Modify the pcost.py program to catch the exception, print a warning message,
# and continue processing the rest of the file.
#------------------------------------------------------------------------------

# import os.path


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# MISSFILE_PATH = BASE + 'Data/missing.csv'

# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     with open(file_name, 'rt') as fi:
#         fi.readline()
#         cnt = 1
#         for line in fi:
#             line = line.strip()
#             cnt += 1
#             try:
#                 _, amount, price = line.split(',')
#                 total += float(amount) * float(price)
#             except ValueError as err:
#                 print(f"Warning: {err} (line: {cnt}) ({line})")
#     return total

# total_cost = portfolio_cost(MISSFILE_PATH)
# print('\nTotal cost:', total_cost)


################################################################################
# Exercise 1.32: Using a library function
# Python comes with a large standard library of useful functions. One library
# that might be useful here is the csv module. You should use it whenever you
# have to work with CSV data files. Here is an example of how it works:

# >>> import csv
# >>> f = open('Data/portfolio.csv')
# >>> rows = csv.reader(f)
# >>> headers = next(rows)
# >>> headers
# ['name', 'shares', 'price']
# >>> for row in rows:
#         print(row)

# ['AA', '100', '32.20']
# ['IBM', '50', '91.10']
# ['CAT', '150', '83.44']
# ['MSFT', '200', '51.23']
# ['GE', '95', '40.37']
# ['MSFT', '50', '65.10']
# ['IBM', '100', '70.44']
# >>> f.close()
# >>>

# One nice thing about the csv module is that it deals with a variety of
# low-level details such as quoting and proper comma splitting. In the above
# output, you’ll notice that it has stripped the double-quotes away from the
# names in the first column.

# Modify your pcost.py program so that it uses the csv module for parsing and
# try running earlier examples.
#------------------------------------------------------------------------------

# import os.path
# import csv


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     with open(file_name, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         cnt = 1
#         for row in rows:
#             cnt += 1
#             try:
#                 total += float(row[1]) * float(row[2])
#             except ValueError as err:
#                 print(f"Warning: {err} (line: {cnt}) ({row})")
#     return total


# total_cost = portfolio_cost(FILE_PATH)
# print('\nTotal cost:', total_cost)


################################################################################
# Exercise 1.33: Reading from the command line
# In the pcost.py program, the name of the input file has been hardwired into
# the code:

    # # pcost.py

    # def portfolio_cost(filename):
    #     ...
    #     # Your code here
    #     ...

    # cost = portfolio_cost('Data/portfolio.csv')
    # print('Total cost:', cost)

# That’s fine for learning and testing, but in a real program you probably
# wouldn’t do that.

# Instead, you might pass the name of the file in as an argument to a script.
# Try changing the bottom part of the program as follows:

    # # pcost.py
    # import sys

    # def portfolio_cost(filename):
    #     ...
    #     # Your code here
    #     ...

    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'

    # cost = portfolio_cost(filename)
    # print('Total cost:', cost)

# sys.argv is a list that contains passed arguments on the command line (if
# any).

# To run your program, you’ll need to run Python from the terminal.

# For example, from bash on Unix:

    # bash % python3 pcost.py Data/portfolio.csv
    # Total cost: 44671.15
    # bash %
#------------------------------------------------------------------------------

import sys
import os.path
import csv


BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
FILE_PATH = BASE + 'Data/portfolio.csv'

def portfolio_cost(file_name: str) -> float:
    total = 0.0
    with open(file_name, 'rt') as fi:
        rows = csv.reader(fi)
        _ = next(rows)
        cnt = 1
        for row in rows:
            cnt += 1
            try:
                total += float(row[1]) * float(row[2])
            except ValueError as err:
                print(f"Warning: {err} (line: {cnt}) ({row})")
    return total


if len(sys.argv) == 2:
    filename = BASE + sys.argv[1]
else:
    filename = FILE_PATH

total_cost = portfolio_cost(filename)
print('\nTotal cost:', total_cost)


################################################################################
