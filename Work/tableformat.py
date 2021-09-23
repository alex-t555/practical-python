""" tableformat.py
"""
###############################################################################
# Exercise 4.5: An Extensibility Problem
# Suppose that you wanted to modify the print_report() function to support a
# variety of different output formats such as plain-text, HTML, CSV, or XML. To
# do this, you could try to write one gigantic function that did everything.
# However, doing so would likely lead to an unmaintainable mess. Instead, this
# is a perfect opportunity to use inheritance instead.

# To start, focus on the steps that are involved in a creating a table. At the
# top of the table is a set of table headers. After that, rows of table data
# appear. Let’s take those steps and put them into their own class. Create a
# file called tableformat.py and define the following class:

# # tableformat.py

# class TableFormatter:
#     def headings(self, headers):
#         '''
#         Emit the table headings.
#         '''
# 	raise NotImplementedError()

#     def row(self, rowdata):
#         '''
#         Emit a single row of table data.
#         '''
# 	raise NotImplementedError()

# This class does nothing, but it serves as a kind of design specification for
# additional classes that will be defined shortly. A class like this is
# sometimes called an “abstract base class.”

# Modify the print_report() function so that it accepts a TableFormatter object
# as input and invokes methods on it to produce the output. For example, like
# this:

# # report.py
# ...

# def print_report(reportdata, formatter):
#     '''
#     Print a nicely formated table from a list of (name, shares, price,
#     change) tuples.
#     '''
#     formatter.headings(['Name','Shares','Price','Change'])
#     for name, shares, price, change in reportdata:
#         rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
#         formatter.row(rowdata)

# Since you added an argument to print_report(), you’re going to need to modify
# the portfolio_report() function as well. Change it so that it creates a
# TableFormatter like this:

# # report.py

# import tableformat

# ...
# def portfolio_report(portfoliofile, pricefile):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     # Read data files
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)

#     # Create the report data
#     report = make_report_data(portfolio, prices)

#     # Print it out
#     formatter = tableformat.TableFormatter()
#     print_report(report, formatter)

# Run this new code:

# >>> ================================ RESTART ================================
# >>> import report
# >>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
# ... crashes ...

# It should immediately crash with a NotImplementedError exception. That’s not
# too exciting, but it’s exactly what we expected. Continue to the next part.
#------------------------------------------------------------------------------

# class TableFormatter:
#     def headings(self, headers):
#         """Emit the table headings."""
#         raise NotImplementedError()

#     def row(self, row):
#         """Emit a single row of table data."""
#         raise NotImplementedError()


###############################################################################
# Exercise 4.6: Using Inheritance to Produce Different Output
# The TableFormatter class you defined in part (a) is meant to be extended via
# inheritance. In fact, that’s the whole idea. To illustrate, define a class
# TextTableFormatter like this:

# # tableformat.py
# ...
# class TextTableFormatter(TableFormatter):
#     '''
#     Emit a table in plain-text format
#     '''
#     def headings(self, headers):
#         for h in headers:
#             print(f'{h:>10s}', end=' ')
#         print()
#         print(('-'*10 + ' ')*len(headers))

#     def row(self, rowdata):
#         for d in rowdata:
#             print(f'{d:>10s}', end=' ')
#         print()

# Modify the portfolio_report() function like this and try it:

# # report.py
# ...
# def portfolio_report(portfoliofile, pricefile):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     # Read data files
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)

#     # Create the report data
#     report = make_report_data(portfolio, prices)

#     # Print it out
#     formatter = tableformat.TextTableFormatter()
#     print_report(report, formatter)

# This should produce the same output as before:

# >>> ================================ RESTART ================================
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

# However, let’s change the output to something else. Define a new class
# CSVTableFormatter that produces output in CSV format:

# # tableformat.py
# ...
# class CSVTableFormatter(TableFormatter):
#     '''
#     Output portfolio data in CSV format.
#     '''
#     def headings(self, headers):
#         print(','.join(headers))

#     def row(self, rowdata):
#         print(','.join(rowdata))

# Modify your main program as follows:

# def portfolio_report(portfoliofile, pricefile):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     # Read data files
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)

#     # Create the report data
#     report = make_report_data(portfolio, prices)

#     # Print it out
#     formatter = tableformat.CSVTableFormatter()
#     print_report(report, formatter)

# You should now see CSV output like this:

# >>> ================================ RESTART ================================
# >>> import report
# >>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
# Name,Shares,Price,Change
# AA,100,9.22,-22.98
# IBM,50,106.28,15.18
# CAT,150,35.46,-47.98
# MSFT,200,20.89,-30.34
# GE,95,13.48,-26.89
# MSFT,50,20.89,-44.21
# IBM,100,106.28,35.84
# Using a similar idea, define a class HTMLTableFormatter that produces a table
# with the following output:

# <tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
# <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
# <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
# <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
# <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
# <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
# <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
# <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

# Test your code by modifying the main program to create a HTMLTableFormatter
# object instead of a CSVTableFormatter object.
#------------------------------------------------------------------------------

# class TableFormatter:

#     def headings(self, headers):
#         """Emit the table headings."""
#         raise NotImplementedError()

#     def row(self, rowdata):
#         """Emit a single row of table data."""
#         raise NotImplementedError()


# class TextTableFormatter(TableFormatter):
#     """Emit a table in plan-text format."""

#     def headings(self, headers):
#         for h in headers:
#             print(f'{h:>10s}', end=' ')
#         print()
#         print(('-'*10 + ' ') * len(headers))

#     def row(self, rowdata):
#         for r in rowdata:
#             print(f'{r:>10s}', end=' ')
#         print()


# class CSVTableFormatter(TableFormatter):
#     """Output portfolio data in CSV format."""

#     def headings(self, headers):
#         print(','.join(headers))

#     def row(self, rowdata):
#         print(','.join(rowdata))


# class HTMLTableFormatter(TableFormatter):
#     """Output portfolio data in HTML format."""

#     def headings(self, headers):
#         print('<tr>', end='')
#         for h in headers:
#             print(f'<th>{h:s}</th>', end='')
#         print('</tr>')

#     def row(self, rowdata):
#         print('<tr>', end='')
#         for r in rowdata:
#             print(f'<td>{r:s}</td>', end='')
#         print('</tr>')


###############################################################################
# Exercise 4.7: Polymorphism in Action
# A major feature of object-oriented programming is that you can plug an object
# into a program and it will work without having to change any of the existing
# code. For example, if you wrote a program that expected to use a
# TableFormatter object, it would work no matter what kind of TableFormatter
# you actually gave it. This behavior is sometimes referred to as
# “polymorphism.”

# One potential problem is figuring out how to allow a user to pick out the
# formatter that they want. Direct use of the class names such as
# TextTableFormatter is often annoying. Thus, you might consider some
# simplified approach. Perhaps you embed an if-statement into the code like
# this:

# def portfolio_report(portfoliofile, pricefile, fmt='txt'):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     # Read data files
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)

#     # Create the report data
#     report = make_report_data(portfolio, prices)

#     # Print it out
#     if fmt == 'txt':
#         formatter = tableformat.TextTableFormatter()
#     elif fmt == 'csv':
#         formatter = tableformat.CSVTableFormatter()
#     elif fmt == 'html':
#         formatter = tableformat.HTMLTableFormatter()
#     else:
#         raise RuntimeError(f'Unknown format {fmt}')
#     print_report(report, formatter)

# In this code, the user specifies a simplified name such as 'txt' or 'csv' to
# pick a format. However, is putting a big if-statement in the
# portfolio_report() function like that the best idea? It might be better to
# move that code to a general purpose function somewhere else.

# In the tableformat.py file, add a function create_formatter(name) that allows
# a user to create a formatter given an output name such as 'txt', 'csv', or
# 'html'. Modify portfolio_report() so that it looks like this:

# def portfolio_report(portfoliofile, pricefile, fmt='txt'):
#     '''
#     Make a stock report given portfolio and price data files.
#     '''
#     # Read data files
#     portfolio = read_portfolio(portfoliofile)
#     prices = read_prices(pricefile)

#     # Create the report data
#     report = make_report_data(portfolio, prices)

#     # Print it out
#     formatter = tableformat.create_formatter(fmt)
#     print_report(report, formatter)

# Try calling the function with different formats to make sure it’s working.
#------------------------------------------------------------------------------

# class TableFormatter:

#     def headings(self, headers):
#         """Emit the table headings."""
#         raise NotImplementedError()

#     def row(self, rowdata):
#         """Emit a single row of table data."""
#         raise NotImplementedError()


# class TextTableFormatter(TableFormatter):
#     """Emit a table in plan-text format."""

#     def headings(self, headers):
#         for h in headers:
#             print(f'{h:>10s}', end=' ')
#         print()
#         print(('-'*10 + ' ') * len(headers))

#     def row(self, rowdata):
#         for r in rowdata:
#             print(f'{r:>10s}', end=' ')
#         print()


# class CSVTableFormatter(TableFormatter):
#     """Output portfolio data in CSV format."""

#     def headings(self, headers):
#         print(','.join(headers))

#     def row(self, rowdata):
#         print(','.join(rowdata))


# class HTMLTableFormatter(TableFormatter):
#     """Output portfolio data in HTML format."""

#     def headings(self, headers):
#         print('<tr>', end='')
#         for h in headers:
#             print(f'<th>{h:s}</th>', end='')
#         print('</tr>')

#     def row(self, rowdata):
#         print('<tr>', end='')
#         for r in rowdata:
#             print(f'<td>{r:s}</td>', end='')
#         print('</tr>')


# def create_formatter(fmt: str) -> TableFormatter:
#     if fmt == 'txt':
#         formatter = TextTableFormatter()
#     elif fmt == 'html':
#         formatter = HTMLTableFormatter()
#     elif fmt == 'csv':
#         formatter = CSVTableFormatter()
#     else:
#         raise RuntimeError(f'Unknown format {fmt}')
#     return formatter


###############################################################################
# Exercise 4.10: An example of using getattr()
# getattr() is an alternative mechanism for reading attributes. It can be used
# to write extremely flexible code. To begin, try this example:

# >>> import stock
# >>> s = stock.Stock('GOOG', 100, 490.1)
# >>> columns = ['name', 'shares']
# >>> for colname in columns:
#         print(colname, '=', getattr(s, colname))

# name = GOOG
# shares = 100
# >>>

# Carefully observe that the output data is determined entirely by the
# attribute names listed in the columns variable.

# In the file tableformat.py, take this idea and expand it into a generalized
# function print_table() that prints a table showing user-specified attributes
# of a list of arbitrary objects. As with the earlier print_report() function,
# print_table() should also accept a TableFormatter instance to control the
# output format. Here’s how it should work:

# >>> import report
# >>> portfolio = report.read_portfolio('Data/portfolio.csv')
# >>> from tableformat import create_formatter, print_table
# >>> formatter = create_formatter('txt')
# >>> print_table(portfolio, ['name','shares'], formatter)
#       name     shares
# ---------- ----------
#         AA        100
#        IBM         50
#        CAT        150
#       MSFT        200
#         GE         95
#       MSFT         50
#        IBM        100

# >>> print_table(portfolio, ['name','shares','price'], formatter)
#       name     shares      price
# ---------- ---------- ----------
#         AA        100       32.2
#        IBM         50       91.1
#        CAT        150      83.44
#       MSFT        200      51.23
#         GE         95      40.37
#       MSFT         50       65.1
#        IBM        100      70.44
# >>>
#------------------------------------------------------------------------------

# from typing import List


# class TableFormatter:

#     def headings(self, headers: List[str]):
#         """Emit the table headings."""
#         raise NotImplementedError()

#     def row(self, rowdata: List[str]):
#         """Emit a single row of table data."""
#         raise NotImplementedError()


# class TextTableFormatter(TableFormatter):
#     """Emit a table in plan-text format."""

#     def headings(self, headers):
#         for h in headers:
#             print(f'{h:>10s}', end=' ')
#         print()
#         print(('-'*10 + ' ') * len(headers))

#     def row(self, rowdata):
#         for r in rowdata:
#             print(f'{r:>10s}', end=' ')
#         print()


# class CSVTableFormatter(TableFormatter):
#     """Output portfolio data in CSV format."""

#     def headings(self, headers):
#         print(','.join(headers))

#     def row(self, rowdata):
#         print(','.join(rowdata))


# class HTMLTableFormatter(TableFormatter):
#     """Output portfolio data in HTML format."""

#     def headings(self, headers):
#         print('<tr>', end='')
#         for h in headers:
#             print(f'<th>{h:s}</th>', end='')
#         print('</tr>')

#     def row(self, rowdata):
#         print('<tr>', end='')
#         for r in rowdata:
#             print(f'<td>{r:s}</td>', end='')
#         print('</tr>')


# def create_formatter(fmt: str) -> TableFormatter:
#     if fmt == 'txt':
#         formatter = TextTableFormatter()
#     elif fmt == 'html':
#         formatter = HTMLTableFormatter()
#     elif fmt == 'csv':
#         formatter = CSVTableFormatter()
#     else:
#         raise RuntimeError(f'Unknown format {fmt}')
#     return formatter


# def print_table(table: List[object], columns: List[str], formatter: TableFormatter):
#     formatter.headings(columns)
#     for row in table:
#         rowdata = [str(getattr(row, col)) for col in columns]
#         formatter.row(rowdata)


###############################################################################
# Exercise 4.11: Defining a custom exception
# It is often good practice for libraries to define their own exceptions.

# This makes it easier to distinguish between Python exceptions raised in
# response to common programming errors versus exceptions intentionally raised
# by a library to a signal a specific usage problem.

# Modify the create_formatter() function from the last exercise so that it
# raises a custom FormatError exception when the user provides a bad format
# name.

# For example:

# >>> from tableformat import create_formatter
# >>> formatter = create_formatter('xls')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "tableformat.py", line 71, in create_formatter
#     raise FormatError('Unknown table format %s' % name)
# FormatError: Unknown table format xls
# >>>
#------------------------------------------------------------------------------

from typing import List


class TableFormatter:

    def headings(self, headers: List[str]):
        """Emit the table headings."""
        raise NotImplementedError()

    def row(self, rowdata: List[str]):
        """Emit a single row of table data."""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """Emit a table in plan-text format."""

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for r in rowdata:
            print(f'{r:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format."""

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML format."""

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h:s}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r:s}</td>', end='')
        print('</tr>')


class FormatError(Exception):
    pass


def create_formatter(fmt: str) -> TableFormatter:
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')
    return formatter


def print_table(table: List[object], columns: List[str], formatter: TableFormatter):
    formatter.headings(columns)
    for row in table:
        rowdata = [str(getattr(row, col)) for col in columns]
        formatter.row(rowdata)


###############################################################################
###############################################################################
