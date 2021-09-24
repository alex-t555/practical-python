#!/usr/bin/env python3
""" pcost.py
"""

###############################################################################
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


###############################################################################
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


###############################################################################
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


###############################################################################
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


###############################################################################
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


###############################################################################
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

# import sys
# import os.path
# import csv


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


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# if len(sys.argv) == 2:
#     filename = BASE + sys.argv[1]
# else:
#     filename = FILE_PATH

# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)


###############################################################################
# Exercise 2.15: A practical enumerate() example
# Recall that the file Data/missing.csv contains data for a stock portfolio,
# but has some rows with missing data. Using enumerate(), modify your pcost.py
# program so that it prints a line number with the warning message when it
# encounters bad input.

# >>> cost = portfolio_cost('Data/missing.csv')
# Row 4: Couldn't convert: ['MSFT', '', '51.23']
# Row 7: Couldn't convert: ['IBM', '', '70.44']
# >>>
# To do this, you’ll need to change a few parts of your code.

# ...
# for rowno, row in enumerate(rows, start=1):
#     try:
#         ...
#     except ValueError:
#         print(f'Row {rowno}: Bad row: {row}')
#------------------------------------------------------------------------------

# import sys
# import os.path
# import csv


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     with open(file_name, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for rowno, row in enumerate(rows, start=2):
#             try:
#                 total += int(row[1]) * float(row[2])
#             except ValueError as err:
#                 print(f"\nWarning: {err} (line {rowno}) ({row})")
#     return total


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# if len(sys.argv) == 2:
#     filename = BASE + sys.argv[1]
# else:
#     filename = FILE_PATH

# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)


###############################################################################
# Exercise 2.16: Using the zip() function
# In the file Data/portfolio.csv, the first line contains column headers. In
# all previous code, we’ve been discarding them.

# >>> f = open('Data/portfolio.csv')
# >>> rows = csv.reader(f)
# >>> headers = next(rows)
# >>> headers
# ['name', 'shares', 'price']
# >>>

# However, what if you could use the headers for something useful? This is
# where the zip() function enters the picture. First try this to pair the file
# headers with a row of data:

# >>> row = next(rows)
# >>> row
# ['AA', '100', '32.20']
# >>> list(zip(headers, row))
# [ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
# >>>

# Notice how zip() paired the column headers with the column values. We’ve used
# list() here to turn the result into a list so that you can see it. Normally,
# zip() creates an iterator that must be consumed by a for-loop.

# This pairing is an intermediate step to building a dictionary. Now try this:

# >>> record = dict(zip(headers, row))
# >>> record
# {'price': '32.20', 'name': 'AA', 'shares': '100'}
# >>>

# This transformation is one of the most useful tricks to know about when
# processing a lot of data files. For example, suppose you wanted to make the
# pcost.py program work with various input files, but without regard for the
# actual column number where the name, shares, and price appear.

# Modify the portfolio_cost() function in pcost.py so that it looks like this:

# # pcost.py

# def portfolio_cost(filename):
#     ...
#         for rowno, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             try:
#                 nshares = int(record['shares'])
#                 price = float(record['price'])
#                 total_cost += nshares * price
#             # This catches errors in int() and float() conversions above
#             except ValueError:
#                 print(f'Row {rowno}: Bad row: {row}')
#         ...

# Now, try your function on a completely different data file
# Data/portfoliodate.csv which looks like this:

# name,date,time,shares,price
# "AA","6/11/2007","9:50am",100,32.20
# "IBM","5/13/2007","4:20pm",50,91.10
# "CAT","9/23/2006","1:30pm",150,83.44
# "MSFT","5/17/2007","10:30am",200,51.23
# "GE","2/1/2006","10:45am",95,40.37
# "MSFT","10/31/2006","12:05pm",50,65.10
# "IBM","7/9/2006","3:15pm",100,70.44

# >>> portfolio_cost('Data/portfoliodate.csv')
# 44671.15
# >>>

# If you did it right, you’ll find that your program still works even though
# the data file has a completely different column format than before. That’s
# cool!

# The change made here is subtle, but significant. Instead of portfolio_cost()
# being hardcoded to read a single fixed file format, the new version reads any
# CSV file and picks the values of interest out of it. As long as the file has
# the required columns, the code will work.

# Modify the report.py program you wrote in Section 2.3 so that it uses the
# same technique to pick out column headers.

# Try running the report.py program on the Data/portfoliodate.csv file and see
# that it produces the same answer as before.
#------------------------------------------------------------------------------

# import sys
# import os.path
# import csv


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     with open(file_name, 'rt') as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=2):
#             record = dict(zip(headers, row))
#             try:
#                 total += int(record['shares']) * float(record['price'])
#             except ValueError as err:
#                 print(f"\nWarning: {err} (line {rowno}) ({row})")
#     return total


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# if len(sys.argv) == 2:
#     filename = BASE + sys.argv[1]
# else:
#     filename = FILE_PATH

# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)

# filename = BASE + 'Data/portfoliodate.csv'
# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)


###############################################################################
# Exercise 3.14: Using more library imports
# In section 1, you wrote a program pcost.py that read a portfolio and computed
# its cost.

# >>> import pcost
# >>> pcost.portfolio_cost('Data/portfolio.csv')
# 44671.15
# >>>

# Modify the pcost.py file so that it uses the report.read_portfolio()
# function.
#------------------------------------------------------------------------------

# import sys
# import os.path

# from report import read_portfolio


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     records = read_portfolio(file_name)
#     for rec in records:
#         total += rec['shares'] * rec['price']
#     return total


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# if len(sys.argv) == 2:
#     filename = BASE + sys.argv[1]
# else:
#     filename = FILE_PATH

# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)

# filename = BASE + 'Data/portfoliodate.csv'
# total_cost = portfolio_cost(filename)
# print('\nTotal cost:', total_cost)


###############################################################################
# Exercise 3.15: main() functions
# In the file report.py add a main() function that accepts a list of command
# line options and produces the same output as before. You should be able to
# run it interatively like this:

# >>> import report
# >>> report.main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84
# >>>

# Modify the pcost.py file so that it has a similar main() function:

# >>> import pcost
# >>> pcost.main(['pcost.py', 'Data/portfolio.csv'])
# Total cost: 44671.15
# >>>
#------------------------------------------------------------------------------

# import os.path

# from report import read_portfolio


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     records = read_portfolio(file_name)
#     for rec in records:
#         total += rec['shares'] * rec['price']
#     return total


# def main(argv: list):
#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_PATH = BASE + 'Data/portfolio.csv'

#     if len(argv) == 2:
#         filename = BASE + sys.argv[1]
#     else:
#         filename = FILE_PATH

#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)

#     filename = BASE + 'Data/portfoliodate.csv'
#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)


# if __name__ == '__main__':
#     import sys
#     main(sys.argv)


###############################################################################
# Exercise 3.16: Making Scripts
# Modify the report.py and pcost.py programs so that they can execute as a
# script on the command line:

# bash $ python3 report.py Data/portfolio.csv Data/prices.csv
#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84

# bash $ python3 pcost.py Data/portfolio.csv
# Total cost: 44671.15
###############################################################################



###############################################################################
# Exercise 4.4: Using your class
# Modify the read_portfolio() function in the report.py program so that it
# reads a portfolio into a list of Stock instances as just shown in Exercise
# 4.3. Once you have done that, fix all of the code in report.py and pcost.py
# so that it works with Stock instances instead of dictionaries.

# Hint: You should not have to make major changes to the code. You will mainly
# be changing dictionary access such as s['shares'] into s.shares.

# You should be able to run your functions the same as before:

# >>> import pcost
# >>> pcost.portfolio_cost('Data/portfolio.csv')
# 44671.15
# >>> import report
# >>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84
# >>>
#------------------------------------------------------------------------------

# import os.path

# from report import read_portfolio


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     records = read_portfolio(file_name)
#     for stock in records:
#         total += stock.shares * stock.price
#     return total


# def main(argv: list):
#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_PATH = BASE + 'Data/portfolio.csv'

#     if len(argv) == 2:
#         filename = BASE + sys.argv[1]
#     else:
#         filename = FILE_PATH

#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)

#     filename = BASE + 'Data/portfoliodate.csv'
#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)


# if __name__ == '__main__':
#     import sys
#     main(sys.argv)


###############################################################################
# Exercise 5.6: Simple Properties
# Properties are a useful way to add “computed attributes” to an object. In stock.py, you created an object Stock. Notice that on your object there is a slight inconsistency in how different kinds of data are extracted:

# >>> from stock import Stock
# >>> s = Stock('GOOG', 100, 490.1)
# >>> s.shares
# 100
# >>> s.price
# 490.1
# >>> s.cost()
# 49010.0
# >>>
# Specifically, notice how you have to add the extra () to cost because it is a method.

# You can get rid of the extra () on cost() if you turn it into a property. Take your Stock class and modify it so that the cost calculation works like this:

# >>> ================================ RESTART ================================
# >>> from stock import Stock
# >>> s = Stock('GOOG', 100, 490.1)
# >>> s.cost
# 49010.0
# >>>
# Try calling s.cost() as a function and observe that it doesn’t work now that cost has been defined as a property.

# >>> s.cost()
# ... fails ...
# >>>
# Making this change will likely break your earlier pcost.py program. You might need to go back and get rid of the () on the cost() method.
#------------------------------------------------------------------------------

# import os.path

# from report import read_portfolio


# def portfolio_cost(file_name: str) -> float:
#     total = 0.0
#     records = read_portfolio(file_name)
#     for stock in records:
#         total += stock.cost
#     return total


# def main(argv: list):
#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_PATH = BASE + 'Data/portfolio.csv'

#     if len(argv) == 2:
#         filename = BASE + sys.argv[1]
#     else:
#         filename = FILE_PATH

#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)

#     filename = BASE + 'Data/portfoliodate.csv'
#     total_cost = portfolio_cost(filename)
#     print('\nTotal cost:', total_cost)


# if __name__ == '__main__':
#     import sys
#     main(sys.argv)


###############################################################################
# Exercise 6.2: Supporting Iteration
# On occasion, you might want to make one of your own objects support
# iteration–especially if your object wraps around an existing list or other
# iterable. In a new file portfolio.py, define the following class:

# # portfolio.py

# class Portfolio:

#     def __init__(self, holdings):
#         self._holdings = holdings

#     @property
#     def total_cost(self):
#         return sum([s.cost for s in self._holdings])

#     def tabulate_shares(self):
#         from collections import Counter
#         total_shares = Counter()
#         for s in self._holdings:
#             total_shares[s.name] += s.shares
#         return total_shares

# This class is meant to be a layer around a list, but with some extra methods
# such as the total_cost property. Modify the read_portfolio() function in
# report.py so that it creates a Portfolio instance like this:

# # report.py
# ...

# import fileparse
# from stock import Stock
# from portfolio import Portfolio

# def read_portfolio(filename):
#     '''
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     '''
#     with open(filename) as file:
#         portdicts = fileparse.parse_csv(file,
#                                         select=['name','shares','price'],
#                                         types=[str,int,float])

#     portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
#     return Portfolio(portfolio)
# ...

# Try running the report.py program. You will find that it fails spectacularly
# due to the fact that Portfolio instances aren’t iterable.

# >>> import report
# >>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
# ... crashes ...

# Fix this by modifying the Portfolio class to support iteration:

# class Portfolio:

#     def __init__(self, holdings):
#         self._holdings = holdings

#     def __iter__(self):
#         return self._holdings.__iter__()

#     @property
#     def total_cost(self):
#         return sum([s.shares*s.price for s in self._holdings])

#     def tabulate_shares(self):
#         from collections import Counter
#         total_shares = Counter()
#         for s in self._holdings:
#             total_shares[s.name] += s.shares
#         return total_shares

# After you’ve made this change, your report.py program should work again.
# While you’re at it, fix up your pcost.py program to use the new Portfolio
# object. Like this:

# # pcost.py

# import report

# def portfolio_cost(filename):
#     '''
#     Computes the total cost (shares*price) of a portfolio file
#     '''
#     portfolio = report.read_portfolio(filename)
#     return portfolio.total_cost
# ...

# Test it to make sure it works:

# >>> import pcost
# >>> pcost.portfolio_cost('Data/portfolio.csv')
# 44671.15
# >>>
#------------------------------------------------------------------------------

import os.path

from report import read_portfolio


def portfolio_cost(file_name: str) -> float:
    portfolio = read_portfolio(file_name)
    return portfolio.total_cost


def main(argv: list):
    BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
    FILE_PATH = BASE + 'Data/portfolio.csv'

    if len(argv) == 2:
        filename = BASE + sys.argv[1]
    else:
        filename = FILE_PATH

    total_cost = portfolio_cost(filename)
    print('\nTotal cost:', total_cost)

    filename = BASE + 'Data/portfoliodate.csv'
    total_cost = portfolio_cost(filename)
    print('\nTotal cost:', total_cost)


if __name__ == '__main__':
    import sys
    main(sys.argv)


###############################################################################
###############################################################################
