""" ticker.py
"""
###############################################################################
# Exercise 6.10: Making more pipeline components
# Let’s extend the whole idea into a larger pipeline. In a separate file
# ticker.py, start by creating a function that reads a CSV file as you did
# above:

# # ticker.py

# from follow import follow
# import csv

# def parse_stock_data(lines):
#     rows = csv.reader(lines)
#     return rows

# if __name__ == '__main__':
#     lines = follow('Data/stocklog.csv')
#     rows = parse_stock_data(lines)
#     for row in rows:
#         print(row)

# Write a new function that selects specific columns:

# # ticker.py
# ...
# def select_columns(rows, indices):
#     for row in rows:
#         yield [row[index] for index in indices]
# ...
# def parse_stock_data(lines):
#     rows = csv.reader(lines)
#     rows = select_columns(rows, [0, 1, 4])
#     return rows

# Run your program again. You should see output narrowed down like this:

# ['BA', '98.35', '0.16']
# ['AA', '39.63', '-0.03']
# ['XOM', '82.45','-0.23']
# ['PG', '62.95', '-0.12']
# ...

# Write generator functions that convert data types and build dictionaries. For
# example:

# # ticker.py
# ...

# def convert_types(rows, types):
#     for row in rows:
#         yield [func(val) for func, val in zip(types, row)]

# def make_dicts(rows, headers):
#     for row in rows:
#         yield dict(zip(headers, row))
# ...
# def parse_stock_data(lines):
#     rows = csv.reader(lines)
#     rows = select_columns(rows, [0, 1, 4])
#     rows = convert_types(rows, [str, float, float])
#     rows = make_dicts(rows, ['name', 'price', 'change'])
#     return rows
# ...

# Run your program again. You should now a stream of dictionaries like this:

# { 'name':'BA', 'price':98.35, 'change':0.16 }
# { 'name':'AA', 'price':39.63, 'change':-0.03 }
# { 'name':'XOM', 'price':82.45, 'change': -0.23 }
# { 'name':'PG', 'price':62.95, 'change':-0.12 }
# ...
#------------------------------------------------------------------------------

# from typing import List, Dict, Generator
# import os.path
# import csv
# import _csv

# from follow import follow


# def select_columns(rows_: _csv.reader,
#                    indices: List[int]) -> Generator[List[str],None,None]:
#     for row_ in rows_:
#         yield [row_[index] for index in indices]


# def convert_types(rows_: List[List[str]],
#                   types: List[type]) -> Generator[List,None,None]:
#     for row_ in rows_:
#         yield [func(val) for func, val in zip(types, row_)]


# def make_dicts(rows_: List,
#                headers: List[str]) -> Generator[Dict,None,None]:
#     for row_ in rows_:
#         yield dict(zip(headers, row_))


# def parse_stock_data(lines_: List[str]) -> List[Dict]:
#     rows_ = csv.reader(lines_)
#     rows_ = select_columns(rows_, [0,1,4])
#     rows_ = convert_types(rows_, [str,float,float])
#     rows_ = make_dicts(rows_, ['name','price','change'])
#     return rows_


# if __name__ == '__main__':

#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

#     lines = follow(FILE_STOCKLOG)
#     rows = parse_stock_data(lines)
#     for row in rows:
#         print(row)


###############################################################################
# Exercise 6.11: Filtering data
# Write a function that filters data. For example:

# # ticker.py
# ...

# def filter_symbols(rows, names):
#     for row in rows:
#         if row['name'] in names:
#             yield row

# Use this to filter stocks to just those in your portfolio:

# import report
# portfolio = report.read_portfolio('Data/portfolio.csv')
# rows = parse_stock_data(follow('Data/stocklog.csv'))
# rows = filter_symbols(rows, portfolio)
# for row in rows:
#     print(row)
#------------------------------------------------------------------------------

# from typing import List, Dict, Generator
# import os.path
# import csv
# import _csv

# from follow import follow


# def select_columns(rows_: _csv.reader,
#                    indices: List[int]) -> Generator[List[str],None,None]:
#     for row_ in rows_:
#         yield [row_[index] for index in indices]


# def convert_types(rows_: List[List[str]],
#                   types: List[type]) -> Generator[List,None,None]:
#     for row_ in rows_:
#         yield [func(val) for func, val in zip(types, row_)]


# def make_dicts(rows_: List,
#                headers: List[str]) -> Generator[Dict,None,None]:
#     for row_ in rows_:
#         yield dict(zip(headers, row_))


# def parse_stock_data(lines_: List[str]) -> List[Dict]:
#     rows_ = csv.reader(lines_)
#     rows_ = select_columns(rows_, [0,1,4])
#     rows_ = convert_types(rows_, [str,float,float])
#     rows_ = make_dicts(rows_, ['name','price','change'])
#     return rows_


# def filter_symbols(rows_: List[Dict],
#                    names: List[str]) -> Generator[Dict,None,None]:
#     for row_ in rows_:
#         if row_['name'] in names:
#             yield row_


# if __name__ == '__main__':

#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

#     lines = follow(FILE_STOCKLOG)
#     rows = parse_stock_data(lines)
#     for row in rows:
#         print(row)


###############################################################################
# Exercise 6.12: Putting it all together
# In the ticker.py program, write a function ticker(portfile, logfile, fmt) that creates a real-time stock ticker from a given portfolio, logfile, and table format. For example::

# >>> from ticker import ticker
# >>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
#       Name      Price     Change
# ---------- ---------- ----------
#         GE      37.14      -0.18
#       MSFT      29.96      -0.09
#        CAT      78.03      -0.49
#         AA      39.34      -0.32
# ...

# >>> ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
# Name,Price,Change
# IBM,102.79,-0.28
# CAT,78.04,-0.48
# AA,39.35,-0.31
# CAT,78.05,-0.47
# ...
#------------------------------------------------------------------------------

from typing import List, Dict, Generator
import os.path
import csv
import _csv

import follow
import report
import tableformat


def select_columns(rows_: _csv.reader,
                   indices: List[int]) -> Generator[List[str],None,None]:
    for row_ in rows_:
        yield [row_[index] for index in indices]


def convert_types(rows_: List[List[str]],
                  types: List[type]) -> Generator[List,None,None]:
    for row_ in rows_:
        yield [func(val) for func, val in zip(types, row_)]


def make_dicts(rows_: List,
               headers: List[str]) -> Generator[Dict,None,None]:
    for row_ in rows_:
        yield dict(zip(headers, row_))


def parse_stock_data(lines_: List[str]) -> List[Dict]:
    rows_ = csv.reader(lines_)
    rows_ = select_columns(rows_, [0,1,4])
    rows_ = convert_types(rows_, [str,float,float])
    rows_ = make_dicts(rows_, ['name','price','change'])
    return rows_


def filter_symbols(rows_: List[Dict],
                   names: List[str]) -> Generator[Dict,None,None]:
    for row_ in rows_:
        if row_['name'] in names:
            yield row_


def ticker(portfoliofile: str, logfile: str, fmt: str='txt'):
    portfolio = report.read_portfolio(portfoliofile)
    rows_ = parse_stock_data(follow.follow(logfile))
    rows_ = filter_symbols(rows_, portfolio)
    formatter = tableformat.create_formatter(fmt)
    headings = ['Name','Price','Change']
    formatter.headings(headings)
    for row_ in rows_:
        rowdata = [str(row_[key.lower()]) for key in headings]
        formatter.row(rowdata)


if __name__ == '__main__':

    BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
    FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

    lines = follow.follow(FILE_STOCKLOG)
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)


###############################################################################
###############################################################################
