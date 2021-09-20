''' report.py
'''

###############################################################################
# Exercise 2.4: A list of tuples
# The file Data/portfolio.csv contains a list of stocks in a portfolio. In
# Exercise 1.30, you wrote a function portfolio_cost(filename) that read this
# file and performed a simple calculation.

# Your code should have looked something like this:

# # pcost.py

#     import csv

#     def portfolio_cost(filename):
#         '''Computes the total cost (shares*price) of a portfolio file'''
#         total_cost = 0.0

#         with open(filename, 'rt') as f:
#             rows = csv.reader(f)
#             headers = next(rows)
#             for row in rows:
#                 nshares = int(row[1])
#                 price = float(row[2])
#                 total_cost += nshares * price
#         return total_cost

# Using this code as a rough guide, create a new file report.py. In that file,
# define a function read_portfolio(filename) that opens a given portfolio file
# and reads it into a list of tuples. To do this, you’re going to make a few
# minor modifications to the above code.
#------------------------------------------------------------------------------

# import os.path
# import csv


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             portfolio.append((row[0], int(row[1]), float(row[2])))
#     return portfolio


# print('\nPortfolio:\n', read_portfolio(FILE_PATH))


###############################################################################
# Exercise 2.5: List of Dictionaries
# Take the function you wrote in Exercise 2.4 and modify to represent each
# stock in the portfolio with a dictionary instead of a tuple. In this
# dictionary use the field names of “name”, “shares”, and “price” to represent
# the different columns in the input file.
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/portfolio.csv'

# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio.append(drow)
#     return portfolio


# print('\nPortfolion')
# pprint(read_portfolio(FILE_PATH))


###############################################################################
# Exercise 2.6: Dictionaries as a container
# The file Data/prices.csv contains a series of lines with stock prices. The
# file looks something like this:

# "AA",9.22
# "AXP",24.85
# "BA",44.85
# "BAC",11.27
# "C",3.72
# ...

# Write a function read_prices(filename) that reads a set of prices such as
# this into a dictionary where the keys of the dictionary are the stock names
# and the values in the dictionary are the stock prices.

# To do this, start with an empty dictionary and start inserting values into it
# just as you did above. However, you are reading the values from a file now.

# We’ll use this data structure to quickly lookup the price of a given stock
# name.

# A few little tips that you’ll need for this part. First, make sure you use
# the csv module just as you did before—there’s no need to reinvent the wheel
# here.

# >>> import csv
# >>> f = open('Data/prices.csv', 'r')
# >>> rows = csv.reader(f)
# >>> for row in rows:
#         print(row)


# ['AA', '9.22']
# ['AXP', '24.85']
# ...
# []
# >>>

# The other little complication is that the Data/prices.csv file may have some
# blank lines in it. Notice how the last row of data above is an empty
# list—meaning no data was present on that line.

# There’s a possibility that this could cause your program to die with an
# exception. Use the try and except statements to catch this as appropriate.
# Thought: would it be better to guard against bad data with an if-statement
# instead?

# Once you have written your read_prices() function, test it interactively to
# make sure it works:

# >>> prices = read_prices('Data/prices.csv')
# >>> prices['IBM']
# 106.28
# >>> prices['MSFT']
# 20.89
# >>>
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PATH = BASE + 'Data/prices.csv'

# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File: \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout

# print('\nPrices:')
# pprint(read_prices(FILE_PATH))


###############################################################################
# Exercise 2.7: Finding out if you can retire
# Tie all of this work together by adding a few additional statements to your
# report.py program that computes gain/loss. These statements should take the
# list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6
# and compute the current value of the portfolio along with the gain/loss.
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio_.append(drow)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = read_portfolio(FILE_PORTFOLIO)
# prices = read_prices(FILE_PRICES)

# gain_loss = {}
# for name, price in prices.items():
#     for stock in portfolio:
#         if stock['name'] == name:
#             gain_loss[name] = gain_loss.setdefault(name, 0) \
#                     + (price - stock['price']) * stock['shares']

# print('\nGain/loss:')
# pprint(gain_loss)


###############################################################################
# Exercise 2.9: Collecting Data
# In Exercise 2.7, you wrote a program called report.py that computed the
# gain/loss of a stock portfolio. In this exercise, you’re going to start
# modifying it to produce a table like this:

#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84

# In this report, “Price” is the current share price of the stock and “Change”
# is the change in the share price from the initial purchase price.

# In order to generate the above report, you’ll first want to collect all of
# the data shown in the table. Write a function make_report() that takes a list
# of stocks and dictionary of prices as input and returns a list of tuples
# containing the rows of the above table.

# Add this function to your report.py file. Here’s how it should work if you
# try it interactively:

# >>> portfolio = read_portfolio('Data/portfolio.csv')
# >>> prices = read_prices('Data/prices.csv')
# >>> report = make_report(portfolio, prices)
# >>> for r in report:
#         print(r)

# ('AA', 100, 9.22, -22.980000000000004)
# ('IBM', 50, 106.28, 15.180000000000007)
# ('CAT', 150, 35.46, -47.98)
# ('MSFT', 200, 20.89, -30.339999999999996)
# ('GE', 95, 13.48, -26.889999999999997)
# ...
# >>>
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio_.append(drow)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                     round(prices_[stock['name']]-stock['price'], 2)))
#     return res


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = read_portfolio(FILE_PORTFOLIO)
# prices = read_prices(FILE_PRICES)
# report = make_report(portfolio, prices)

# print('\nReport:')
# pprint(report)


###############################################################################
# Exercise 2.10: Printing a formatted table
# Redo the for-loop in Exercise 2.9, but change the print statement to format
# the tuples.

# >>> for r in report:
#         print('%10s %10d %10.2f %10.2f' % r)

#           AA        100       9.22     -22.98
#          IBM         50     106.28      15.18
#          CAT        150      35.46     -47.98
#         MSFT        200      20.89     -30.34
# ...
# >>>

# You can also expand the values and use f-strings. For example:

# >>> for name, shares, price, change in report:
#         print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

#           AA        100       9.22     -22.98
#          IBM         50     106.28      15.18
#          CAT        150      35.46     -47.98
#         MSFT        200      20.89     -30.34
# ...
# >>>

# Take the above statements and add them to your report.py program. Have your
# program take the output of the make_report() function and print a nicely
# formatted table as shown.
#------------------------------------------------------------------------------

# import os.path
# import csv


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio_.append(drow)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                     round(prices_[stock['name']]-stock['price'], 2)))
#     return res


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = read_portfolio(FILE_PORTFOLIO)
# prices = read_prices(FILE_PRICES)
# report = make_report(portfolio, prices)

# print('\nReport:')
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


###############################################################################
# Exercise 2.11: Adding some headers
# Suppose you had a tuple of header names like this:

# headers = ('Name', 'Shares', 'Price', 'Change')

# Add code to your program that takes the above tuple of headers and creates a
# string where each header name is right-aligned in a 10-character wide field
# and each field is separated by a single space.

# '      Name     Shares      Price      Change'

# Write code that takes the headers and creates the separator string between
# the headers and data to follow. This string is just a bunch of “-“ characters
# under each field name. For example:

# '---------- ---------- ---------- -----------'

# When you’re done, your program should produce the table shown at the top of
# this exercise.

#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100       9.22     -22.98
#        IBM         50     106.28      15.18
#        CAT        150      35.46     -47.98
#       MSFT        200      20.89     -30.34
#         GE         95      13.48     -26.89
#       MSFT         50      20.89     -44.21
#        IBM        100     106.28      35.84
#------------------------------------------------------------------------------

# import os.path
# import csv


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio_.append(drow)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                     round(prices_[stock['name']]-stock['price'], 2)))
#     return res


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = read_portfolio(FILE_PORTFOLIO)
# prices = read_prices(FILE_PRICES)
# report = make_report(portfolio, prices)

# print('\nReport:')
# print('{:>10s} {:>10s} {:>10s} {:>10s}'\
#       .format('Name', 'Shares', 'Price', 'Change'))
# print(('-'*10+' ')*4)
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


###############################################################################
# Exercise 2.12: Formatting Challenge
# How would you modify your code so that the price includes the currency symbol ($) and the output looks like this:

#       Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#         AA        100      $9.22     -22.98
#        IBM         50    $106.28      15.18
#        CAT        150     $35.46     -47.98
#       MSFT        200     $20.89     -30.34
#         GE         95     $13.48     -26.89
#       MSFT         50     $20.89     -44.21
#        IBM        100    $106.28      35.84
#------------------------------------------------------------------------------

# import os.path
# import csv


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         _ = next(rows)
#         for row in rows:
#             drow = {
#                 'name': row[0],
#                 'shares': int(row[1]),
#                 'price': float(row[2])
#             }
#             portfolio_.append(drow)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     dout = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for i, row in enumerate(rows):
#             try:
#                 dout[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {i+1}',
#                       f'\n    ({row})')
#     return dout


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                     round(prices_[stock['name']]-stock['price'], 2)))
#     return res


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = read_portfolio(FILE_PORTFOLIO)
# prices = read_prices(FILE_PRICES)
# report = make_report(portfolio, prices)

# print('\nReport:')
# print('{:>10s} {:>10s} {:>10s} {:>10s}'\
#       .format('Name', 'Shares', 'Price', 'Change'))
# print(('-'*10+' ')*4)
# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d}",
#           f"{'$'+str(round(price, 2)):>10s} {change:>10.2f}")


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

# import os.path
# import csv


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=2):
#             try:
#                 i = headers.index('shares')
#                 j = headers.index('price')
#                 row[i] = int(row[i])
#                 row[j] = float(row[j])
#             except (ValueError, IndexError) as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    ({row})')
#                 continue
#             record = dict(zip(headers, row))
#             portfolio_.append(record)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     prices_ = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for rowno, row in enumerate(rows, start=1):
#             try:
#                 prices_[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    ({row})')
#     return prices_


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         try:
#             res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                         round(prices_[stock['name']]-stock['price'], 2)))
#         except KeyError as err:
#             print(f'\nWarning: {err}',
#                   f'\n  ({stock})')
#     return res


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PORTFOLIODATE = BASE + 'Data/portfoliodate.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# prices = read_prices(FILE_PRICES)

# portfolio = read_portfolio(FILE_PORTFOLIO)
# report = make_report(portfolio, prices)

# print('\nReport:')
# print('{:>10s} {:>10s} {:>10s} {:>10s}'\
#     .format('Name', 'Shares', 'Price', 'Change'))
# print(('-'*10+' ')*4)
# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d}",
#         f"{'$'+str(round(price, 2)):>10s} {change:>10.2f}")

# portfoliodate = read_portfolio(FILE_PORTFOLIODATE)
# report = make_report(portfoliodate, prices)

# print('\nReport:')
# print('{:>10s} {:>10s} {:>10s} {:>10s}'\
#     .format('Name', 'Shares', 'Price', 'Change'))
# print(('-'*10+' ')*4)
# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d}",
#         f"{'$'+str(round(price, 2)):>10s} {change:>10.2f}")


###############################################################################
# Exercise 3.1: Structuring a program as a collection of functions
# Modify your report.py program so that all major operations, including
# calculations and output, are carried out by a collection of functions.
# Specifically:
#     - Create a function print_report(report) that prints out the report.
#     - Change the last part of the program so that it is nothing more than a
#     series of function calls and no other computation.
#------------------------------------------------------------------------------

# import os.path
# import csv


# def read_portfolio(filename: str) -> list:
#     '''Read a portfolio file'''
#     portfolio_ = []
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=2):
#             try:
#                 i = headers.index('shares')
#                 j = headers.index('price')
#                 row[i] = int(row[i])
#                 row[j] = float(row[j])
#             except (ValueError, IndexError) as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    ({row})')
#                 continue
#             record = dict(zip(headers, row))
#             portfolio_.append(record)
#     return portfolio_


# def read_prices(filename: str) -> dict:
#     '''Read a prices file'''
#     prices_ = {}
#     with open(filename, 'rt') as fi:
#         rows = csv.reader(fi)
#         for rowno, row in enumerate(rows, start=1):
#             try:
#                 prices_[row[0]] = float(row[1])
#             except IndexError as err:
#                 print(f'\nWarning: {err}',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    ({row})')
#     return prices_


# def make_report(portfolio_: list, prices_: dict) -> list:
#     '''Make report'''
#     res = []
#     for stock in portfolio_:
#         try:
#             res.append((stock['name'], stock['shares'], prices_[stock['name']],
#                         round(prices_[stock['name']]-stock['price'], 2)))
#         except KeyError as err:
#             print(f'\nWarning: {err}',
#                   f'\n  ({stock})')
#     return res


# def print_report(report_: list):
#     print('\nReport:')
#     print('{:>10s} {:>10s} {:>10s} {:>10s}'\
#         .format('Name', 'Shares', 'Price', 'Change'))
#     print(('-'*10+' ')*4)
#     for name, shares, price, change in report_:
#         print(f"{name:>10s} {shares:>10d}",
#             f"{'$'+str(round(price, 2)):>10s} {change:>10.2f}")


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PORTFOLIODATE = BASE + 'Data/portfoliodate.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# prices = read_prices(FILE_PRICES)

# portfolio = read_portfolio(FILE_PORTFOLIO)
# report = make_report(portfolio, prices)
# print_report(report)


# portfoliodate = read_portfolio(FILE_PORTFOLIODATE)
# report = make_report(portfoliodate, prices)
# print_report(report)


###############################################################################
# Exercise 3.2: Creating a top-level function for program execution
# Take the last part of your program and package it into a single function
# portfolio_report(portfolio_filename, prices_filename). Have the function work
# so that the following function call creates the report as before:

#     portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

# In this final version, your program will be nothing more than a series of
# function definitions followed by a single function call to portfolio_report()
# at the very end (which executes all of the steps involved in the program).

# By turning your program into a single function, it becomes easy to run it on
# different inputs. For example, try these statements interactively after
# running your program:

# >>> portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')
# ... look at the output ...
# >>> files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
# >>> for name in files:
#         print(f'{name:-^43s}')
#         portfolio_report(name, 'Data/prices.csv')
#         print()

# ... look at the output ...
# >>>
#------------------------------------------------------------------------------

import os.path
import csv


def read_portfolio(filename: str) -> list:
    '''Read a portfolio file'''
    portfolio_ = []
    with open(filename, 'rt') as fi:
        rows = csv.reader(fi)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=2):
            try:
                i = headers.index('shares')
                j = headers.index('price')
                row[i] = int(row[i])
                row[j] = float(row[j])
            except (ValueError, IndexError) as err:
                print(f'\nWarning: {err}',
                      f'\n  File \"{filename}\", line {rowno}',
                      f'\n    ({row})')
                continue
            record = dict(zip(headers, row))
            portfolio_.append(record)
    return portfolio_


def read_prices(filename: str) -> dict:
    '''Read a prices file'''
    prices_ = {}
    with open(filename, 'rt') as fi:
        rows = csv.reader(fi)
        for rowno, row in enumerate(rows, start=1):
            try:
                prices_[row[0]] = float(row[1])
            except IndexError as err:
                print(f'\nWarning: {err}',
                      f'\n  File \"{filename}\", line {rowno}',
                      f'\n    ({row})')
    return prices_


def make_report(portfolio_: list, prices_: dict) -> list:
    '''Make report'''
    res = []
    for stock in portfolio_:
        try:
            res.append((stock['name'], stock['shares'], prices_[stock['name']],
                        round(prices_[stock['name']]-stock['price'], 2)))
        except KeyError as err:
            print(f'\nWarning: {err}',
                  f'\n  ({stock})')
    return res


def print_report(report_: list):
    print('\nReport:')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'\
        .format('Name', 'Shares', 'Price', 'Change'))
    print(('-'*10+' ')*4)
    for name, shares, price, change in report_:
        print(f"{name:>10s} {shares:>10d}",
            f"{'$'+str(round(price, 2)):>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio_ = read_portfolio(portfolio_filename)
    prices_ = read_prices(prices_filename)
    report_ = make_report(portfolio_, prices_)
    print_report(report_)


BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
FILE_PORTFOLIODATE = BASE + 'Data/portfoliodate.csv'
FILE_PRICES = BASE + 'Data/prices.csv'

portfolio_report(FILE_PORTFOLIO, FILE_PRICES)

portfolio_report(FILE_PORTFOLIODATE, FILE_PRICES)


###############################################################################
###############################################################################
