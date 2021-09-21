""" fileparse.py
"""
###############################################################################
# Exercise 3.3: Reading CSV Files
# To start, let’s just focus on the problem of reading a CSV file into a list
# of dictionaries. In the file fileparse.py, define a function that looks like
# this:

# # fileparse.py
#     import csv

#     def parse_csv(filename):
#         '''
#         Parse a CSV file into a list of records
#         '''
#         with open(filename) as f:
#             rows = csv.reader(f)

#             # Read the file headers
#             headers = next(rows)
#             records = []
#             for row in rows:
#                 if not row:    # Skip rows with no data
#                     continue
#                 record = dict(zip(headers, row))
#                 records.append(record)

#         return records

# This function reads a CSV file into a list of dictionaries while hiding the
# details of opening the file, wrapping it with the csv module, ignoring blank
# lines, and so forth.

# Try it out:

# Hint: python3 -i fileparse.py.

# >>> portfolio = parse_csv('Data/portfolio.csv')
# >>> portfolio
# [{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
# >>>

# This is good except that you can’t do any kind of useful calculation with the
# data because everything is represented as a string. We’ll fix this shortly,
# but let’s keep building on it.
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str) -> list:
#     """Parse a CSV file into a list of records"""
#     records = []
#     with open(filename) as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         for rowno, row in enumerate(rows, start=2):
#             if len(row) != len(headers):
#                 print('\nWarning: number of elements in the headers and row does not match',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    {row}')
#                 continue
#             record = dict(zip(headers, row))
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.4: Building a Column Selector
# In many cases, you’re only interested in selected columns from a CSV file,
# not all of the data. Modify the parse_csv() function so that it optionally
# allows user-specified columns to be picked out as follows:

# >>> # Read all of the data
# >>> portfolio = parse_csv('Data/portfolio.csv')
# >>> portfolio
# [{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10',
# 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares':
# '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price':
# '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT',
# 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]

# >>> # Read only some of the data
# >>> shares_held = parse_csv('Data/portfolio.csv', select=['name','shares'])
# >>> shares_held
# [{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name':
# 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE',
# 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares':
# '100'}]
# >>>

# An example of a column selector was given in Exercise 2.23. However, here’s
# one way to do it:

# # fileparse.py
# import csv

# def parse_csv(filename, select=None):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     with open(filename) as f:
#         rows = csv.reader(f)

#         # Read the file headers
#         headers = next(rows)

#         # If a column selector was given, find indices of the specified columns.
#         # Also narrow the set of headers used for resulting dictionaries
#         if select:
#             indices = [headers.index(colname) for colname in select]
#             headers = select
#         else:
#             indices = []

#         records = []
#         for row in rows:
#             if not row:    # Skip rows with no data
#                 continue
#             # Filter the row if specific columns were selected
#             if indices:
#                 row = [ row[index] for index in indices ]

#             # Make a dictionary
#             record = dict(zip(headers, row))
#             records.append(record)

#     return records

# There are a number of tricky bits to this part. Probably the most important
# one is the mapping of the column selections to row indices. For example,
# suppose the input file had the following headers:

# >>> headers = ['name', 'date', 'time', 'shares', 'price']
# >>>

# Now, suppose the selected columns were as follows:

# >>> select = ['name', 'shares']
# >>>

# To perform the proper selection, you have to map the selected column names to
# column indices in the file. That’s what this step is doing:

# >>> indices = [headers.index(colname) for colname in select ]
# >>> indices
# [0, 3]
# >>>

# In other words, “name” is column 0 and “shares” is column 3. When you read a
# row of data from the file, the indices are used to filter it:

# >>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
# >>> row = [ row[index] for index in indices ]
# >>> row
# ['AA', '100']
# >>>
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str, select: list=None) -> list:
#     """Parse a CSV file into a list of records"""
#     records = []
#     with open(filename) as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(s) for s in select]
#             headers = select
#         else:
#             indices = []
#         for rowno, row in enumerate(rows, start=2):
#             if not row:
#                 print('\nWarning: number of elements in the headers and row does not match',
#                       f'\n  File \"{filename}\", line {rowno}',
#                       f'\n    {row}')
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             record = dict(zip(headers, row))
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.5: Performing Type Conversion
# Modify the parse_csv() function so that it optionally allows type-conversions
# to be applied to the returned data. For example:

# >>> portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
# >>> portfolio
# [{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM',
# 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price':
# 51.23, 'name': 'MSFT', 'shares': 200}, {'price': 40.37, 'name': 'GE',
# 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price':
# 70.44, 'name': 'IBM', 'shares': 100}]

# >>> shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'],
# types=[str, int])
# >>> shares_held
# [{'name': 'AA', 'shares': 100}, {'name': 'IBM', 'shares': 50}, {'name':
# 'CAT', 'shares': 150}, {'name': 'MSFT', 'shares': 200}, {'name': 'GE',
# 'shares': 95}, {'name': 'MSFT', 'shares': 50}, {'name': 'IBM', 'shares':
# 100}]
# >>>

# You already explored this in Exercise 2.24. You’ll need to insert the
# following fragment of code into your solution:

# ...
# if types:
#     row = [func(val) for func, val in zip(types, row) ]
# ...
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str, select: list=None, types: list=None) -> list:
#     """Parse a CSV file into a list of records"""
#     records = []
#     with open(filename) as fi:
#         rows = csv.reader(fi)
#         headers = next(rows)
#         if select:
#             indices = [headers.index(s) for s in select]
#             headers = [headers[j] for j in indices]
#         else:
#             indices = []
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             record = dict(zip(headers, row))
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.6: Working without Headers
# Some CSV files don’t include any header information. For example, the file
# prices.csv looks like this:

# "AA",9.22
# "AXP",24.85
# "BA",44.85
# "BAC",11.27
# ...

# Modify the parse_csv() function so that it can work with such files by
# creating a list of tuples instead. For example:

# >>> prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
# >>> prices
# [('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72),
# ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48),
# ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC',
# 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD',
# 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19),
# ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74),
# ('XOM', 69.35)]
# >>>
# To make this change, you’ll need to modify the code so that the first line of # data isn’t interpreted as a header line. Also, you’ll need to make sure you
# don’t create dictionaries as there are no longer any column names to use for
# keys.
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str,
#               select: list=None,
#               types: list=None,
#               has_headers: bool=True) -> list:
#     """Parse a CSV file into a list of records"""
#     records = []
#     with open(filename) as fi:
#         rows = csv.reader(fi)
#         indices = None
#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(s) for s in select]
#                 headers = [headers[j] for j in indices]
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             if has_headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PRICES, types=[str, float], has_headers=False)
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.7: Picking a different column delimitier
# Although CSV files are pretty common, it’s also possible that you could
# encounter a file that uses a different column separator such as a tab or
# space. For example, the file Data/portfolio.dat looks like this:

# name shares price
# "AA" 100 32.20
# "IBM" 50 91.10
# "CAT" 150 83.44
# "MSFT" 200 51.23
# "GE" 95 40.37
# "MSFT" 50 65.10
# "IBM" 100 70.44

# The csv.reader() function allows a different column delimiter to be given as
# follows:

# rows = csv.reader(f, delimiter=' ')

# Modify your parse_csv() function so that it also allows the delimiter to be
# changed.

# For example:

# >>> portfolio = parse_csv('Data/portfolio.dat',
#                           types=[str, int, float],
#                           delimiter=' ')
# >>> portfolio
# [{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10',
# 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares':
# '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price':
# '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT',
# 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
# >>>
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str,
#               select: list=None,
#               types: list=None,
#               has_headers: bool=True,
#               delimiter: str=',') -> list:
#     """Parse a CSV file into a list of records"""
#     records = []
#     with open(filename, newline='') as fi:
#         rows = csv.reader(fi, delimiter=delimiter)
#         indices = []
#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(s) for s in select]
#                 headers = [headers[j] for j in indices]
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             if has_headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PORTFOLIO_DAT = BASE + 'Data/portfolio.dat'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PRICES, types=[str, float], has_headers=False)
# print('\nPrices:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO_DAT,
#                       types=[str, int, float],
#                       delimiter=' ')
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.8: Raising exceptions
# The parse_csv() function you wrote in the last section allows user-specified
# columns to be selected, but that only works if the input data file has column
# headers.

# Modify the code so that an exception gets raised if both the select and
# has_headers=False arguments are passed. For example:

# >>> parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "fileparse.py", line 9, in parse_csv
#     raise RuntimeError("select argument requires column headers")
# RuntimeError: select argument requires column headers
# >>>

# Having added this one check, you might ask if you should be performing other
# kinds of sanity checks in the function. For example, should you check that
# the filename is a string, that types is a list, or anything of that nature?

# As a general rule, it’s usually best to skip such tests and to just let the
# program fail on bad inputs. The traceback message will point at the source of
# the problem and can assist in debugging.

# The main reason for adding the above check is to avoid running the code in a
# non-sensical mode (e.g., using a feature that requires column headers, but
# simultaneously specifying that there are no headers).

# This indicates a programming error on the part of the calling code. Checking
# for cases that “aren’t supposed to happen” is often a good idea.
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str,
#               select: list=None,
#               types: list=None,
#               has_headers: bool=True,
#               delimiter: str=',') -> list:
#     """Parse a CSV file into a list of records"""
#     if select and not has_headers:
#         raise RuntimeError('select argument requires column headers')
#     records = []
#     with open(filename, newline='') as fi:
#         rows = csv.reader(fi, delimiter=delimiter)
#         indices = []
#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(s) for s in select]
#                 headers = [headers[j] for j in indices]
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             if types:
#                 row = [func(val) for func, val in zip(types, row)]
#             if has_headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PORTFOLIO_DAT = BASE + 'Data/portfolio.dat'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)

# prices = parse_csv(FILE_PRICES, types=[str, float], has_headers=False)
# print('\nPrices:')
# pprint(prices)

# portfolio = parse_csv(FILE_PORTFOLIO_DAT,
#                       types=[str, int, float],
#                       delimiter=' ')
# print('\nPortfolio:')
# pprint(portfolio)

# try:
#     prices = parse_csv(FILE_PRICES, select=['name','price'], has_headers=False)
# except RuntimeError as err:
#     print(f'\nError: in parse_csv(...), {err}')
# else:
#     print('\nPrices:')
#     pprint(prices)


###############################################################################
# Exercise 3.9: Catching exceptions
# The parse_csv() function you wrote is used to process the entire contents of
# a file. However, in the real-world, it’s possible that input files might have
# corrupted, missing, or dirty data. Try this experiment:

# >>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "fileparse.py", line 36, in parse_csv
#     row = [func(val) for func, val in zip(types, row)]
# ValueError: invalid literal for int() with base 10: ''
# >>>

# Modify the parse_csv() function to catch all ValueError exceptions generated
# during record creation and print a warning message for rows that can’t be
# converted.

# The message should include the row number and information about the reason
# why it failed. To test your function, try reading the file Data/missing.csv
# above. For example:

# >>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
# Row 4: Couldn't convert ['MSFT', '', '51.23']
# Row 4: Reason invalid literal for int() with base 10: ''
# Row 7: Couldn't convert ['IBM', '', '70.44']
# Row 7: Reason invalid literal for int() with base 10: ''
# >>>
# >>> portfolio
# [{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM',
# 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price':
# 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares':
# 50}]
# >>>
#------------------------------------------------------------------------------

# import os.path
# import csv
# from pprint import pprint


# def parse_csv(filename: str,
#               select: list=None,
#               types: list=None,
#               has_headers: bool=True,
#               delimiter: str=',') -> list:
#     """Parse a CSV file into a list of records"""
#     if select and not has_headers:
#         raise RuntimeError('select argument requires column headers')
#     records = []
#     with open(filename, newline='') as fi:
#         rows = csv.reader(fi, delimiter=delimiter)
#         indices = []
#         headers = []
#         if has_headers:
#             headers = next(rows)
#             if select:
#                 indices = [headers.index(s) for s in select]
#                 headers = [headers[j] for j in indices]
#         for rowno, row in enumerate(rows, start=2):
#             if not row:
#                 continue
#             if indices:
#                 row = [row[i] for i in indices]
#             if types:
#                 try:
#                     row = [func(val) for func, val in zip(types, row)]
#                 except ValueError as e:
#                     print(f'Row {rowno}: Could not convert {row}')
#                     print(f'Row {rowno}: Reason {e}')
#                     continue
#             if has_headers:
#                 record = dict(zip(headers, row))
#             else:
#                 record = tuple(row)
#             records.append(record)
#     return records


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
# FILE_PORTFOLIO_DAT = BASE + 'Data/portfolio.dat'
# FILE_MISSING = BASE + 'Data/missing.csv'
# FILE_PRICES = BASE + 'Data/prices.csv'

# portfolio = parse_csv(FILE_PORTFOLIO)
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, select=['name', 'price'])
# print('\nPortfolio:')
# pprint(portfolio)

# portfolio = parse_csv(FILE_PORTFOLIO, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)

# prices = parse_csv(FILE_PRICES, types=[str, float], has_headers=False)
# print('\nPrices:')
# pprint(prices)

# portfolio = parse_csv(FILE_PORTFOLIO_DAT,
#                       types=[str, int, float],
#                       delimiter=' ')
# print('\nPortfolio:')
# pprint(portfolio)

# try:
#     prices = parse_csv(FILE_PRICES, select=['name','price'], has_headers=False)
# except RuntimeError as err:
#     print(f'\nError: in parse_csv(...), {err}')
# else:
#     print('\nPrices:')
#     pprint(prices)


# portfolio = parse_csv(FILE_MISSING, types=[str, int, float])
# print('\nPortfolio:')
# pprint(portfolio)


###############################################################################
# Exercise 3.10: Silencing Errors
# Modify the parse_csv() function so that parsing error messages can be
# silenced if explicitly desired by the user. For example:

# >>> portfolio = parse_csv('Data/missing.csv', types=[str,int,float],
# silence_errors=True)
# >>> portfolio
# [{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM',
# 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price':
# 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares':
# 50}]
# >>>
# Error handling is one of the most difficult things to get right in most
# programs. As a general rule, you shouldn’t silently ignore errors. Instead,
# it’s better to report problems and to give the user an option to the silence
# the error message if they choose to do so.
#------------------------------------------------------------------------------

import os.path
import csv
from pprint import pprint


def parse_csv(filename: str,
              select: list=None,
              types: list=None,
              has_headers: bool=True,
              delimiter: str=',',
              silence_errors: bool=False) -> list:
    """Parse a CSV file into a list of records"""
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    records = []
    with open(filename, newline='') as fi:
        rows = csv.reader(fi, delimiter=delimiter)
        indices = []
        headers = []
        lineno = 0
        if has_headers:
            headers = next(rows)
            lineno = 1
            if select:
                indices = [headers.index(s) for s in select]
                headers = [headers[j] for j in indices]
        for row in rows:
            lineno += 1
            if not row:
                continue
            if indices:
                row = [row[i] for i in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {lineno}: Could not convert {row}')
                        print(f'Row {lineno}: Reason {e}')
                    continue
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records


if __name__ == '__main__':
    BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
    FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
    FILE_PORTFOLIO_DAT = BASE + 'Data/portfolio.dat'
    FILE_MISSING = BASE + 'Data/missing.csv'
    FILE_PRICES = BASE + 'Data/prices.csv'

    print('\nPortfolio:')
    portfolio = parse_csv(FILE_PORTFOLIO)
    pprint(portfolio)

    print('\nPortfolio:')
    portfolio = parse_csv(FILE_PORTFOLIO, select=['name','price'])
    pprint(portfolio)

    print('\nPortfolio:')
    portfolio = parse_csv(FILE_PORTFOLIO, types=[str,int,float])
    pprint(portfolio)

    print('\nPrices:')
    prices = parse_csv(FILE_PRICES, types=[str,float], has_headers=False)
    pprint(prices)

    print('\nPortfolio:')
    portfolio = parse_csv(FILE_PORTFOLIO_DAT,
                        types=[str,int,float],
                        delimiter=' ')
    pprint(portfolio)

    print('\nPrices:')
    try:
        prices = parse_csv(FILE_PRICES, select=['name','price'], has_headers=False)
    except RuntimeError as err:
        print(f'\nError: in parse_csv(...), {err}\n')
    else:
        pprint(prices)


    print('\nPortfolio:')
    portfolio = parse_csv(FILE_MISSING, types=[str,int,float])
    pprint(portfolio)

    print('\nPortfolio:')
    portfolio = parse_csv(FILE_MISSING, types=[str,int,float], silence_errors=True)
    pprint(portfolio)


###############################################################################
###############################################################################
