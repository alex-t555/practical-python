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
#                 print(f'Warning: {err}',
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

import os.path
import csv
from pprint import pprint


def read_portfolio(filename: str) -> list:
    '''Read a portfolio file'''
    portfolio_ = []
    with open(filename, 'rt') as fi:
        rows = csv.reader(fi)
        _ = next(rows)
        for row in rows:
            drow = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio_.append(drow)
    return portfolio_


def read_prices(filename: str) -> dict:
    '''Read a prices file'''
    dout = {}
    with open(filename, 'rt') as fi:
        rows = csv.reader(fi)
        _ = next(rows)
        for i, row in enumerate(rows):
            try:
                dout[row[0]] = float(row[1])
            except IndexError as err:
                print(f'Warning: {err}',
                      f'\n  File \"{filename}\", line {i+1}',
                      f'\n    ({row})')
    return dout


BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
FILE_PRICES = BASE + 'Data/prices.csv'

portfolio = read_portfolio(FILE_PORTFOLIO)
prices = read_prices(FILE_PRICES)

gain_loss = {}
for name, price in prices.items():
    for stock in portfolio:
        if stock['name'] == name:
            gain_loss[name] = gain_loss.setdefault(name, 0) \
                    + (price - stock['price']) * stock['shares']

print('\nGain/loss:')
pprint(gain_loss)


###############################################################################
