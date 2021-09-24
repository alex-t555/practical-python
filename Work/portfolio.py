""" portfolio.py
"""
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

# from collections import Counter


# class Portfolio:

#     def __init__(self, holdings):
#         self._holdings = holdings

#     def __iter__(self):
#         return self._holdings.__iter__()

#     @property
#     def total_cost(self):
#         return sum([stock.cost for stock in self._holdings])

#     def tabulate_shares(self):
#         total_shares = Counter()
#         for stock in self._holdings:
#             total_shares[stock.name] += stock.shares
#         return total_shares


###############################################################################
# Exercise 6.3: Making a more proper container
# If making a container class, you often want to do more than just iteration.
# Modify the Portfolio class so that it has some other special methods like
# this:

# class Portfolio:
#     def __init__(self, holdings):
#         self._holdings = holdings

#     def __iter__(self):
#         return self._holdings.__iter__()

#     def __len__(self):
#         return len(self._holdings)

#     def __getitem__(self, index):
#         return self._holdings[index]

#     def __contains__(self, name):
#         return any([s.name == name for s in self._holdings])

#     @property
#     def total_cost(self):
#         return sum([s.shares*s.price for s in self._holdings])

#     def tabulate_shares(self):
#         from collections import Counter
#         total_shares = Counter()
#         for s in self._holdings:
#             total_shares[s.name] += s.shares
#         return total_shares

# Now, try some experiments using this new class:

# >>> import report
# >>> portfolio = report.read_portfolio('Data/portfolio.csv')
# >>> len(portfolio)
# 7
# >>> portfolio[0]
# Stock('AA', 100, 32.2)
# >>> portfolio[1]
# Stock('IBM', 50, 91.1)
# >>> portfolio[0:3]
# [Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
# >>> 'IBM' in portfolio
# True
# >>> 'AAPL' in portfolio
# False
# >>>

# One important observation about this–generally code is considered “Pythonic”
# if it speaks the common vocabulary of how other parts of Python normally
# work. For container objects, supporting iteration, indexing, containment, and
# other kinds of operators is an important part of this.
#------------------------------------------------------------------------------

from collections import Counter


class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any((s.name == name for s in self._holdings))

    @property
    def total_cost(self):
        return sum([stock.cost for stock in self._holdings])

    def tabulate_shares(self):
        total_shares = Counter()
        for stock in self._holdings:
            total_shares[stock.name] += stock.shares
        return total_shares


###############################################################################
###############################################################################
