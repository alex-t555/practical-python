""" stock.py
"""
###############################################################################
# Exercise 4.1: Objects as Data Structures
# In section 2 and 3, we worked with data represented as tuples and
# dictionaries. For example, a holding of stock could be represented as a tuple
# like this:

# s = ('GOOG',100,490.10)
# or as a dictionary like this:

# s = { 'name'   : 'GOOG',
#       'shares' : 100,
#       'price'  : 490.10
# }
# You can even write functions for manipulating such data. For example:

# def cost(s):
#     return s['shares'] * s['price']
# However, as your program gets large, you might want to create a better sense
# of organization. Thus, another approach for representing data would be to
# define a class. Create a file called stock.py and define a class Stock that
# represents a single holding of stock. Have the instances of Stock have name,
# shares, and price attributes. For example:

# >>> import stock
# >>> a = stock.Stock('GOOG',100,490.10)
# >>> a.name
# 'GOOG'
# >>> a.shares
# 100
# >>> a.price
# 490.1
# >>>

# Create a few more Stock objects and manipulate them. For example:

# >>> b = stock.Stock('AAPL', 50, 122.34)
# >>> c = stock.Stock('IBM', 75, 91.75)
# >>> b.shares * b.price
# 6117.0
# >>> c.shares * c.price
# 6881.25
# >>> stocks = [a, b, c]
# >>> stocks
# [<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>,
# <stock.Stock object at 0x37d050>]
# >>> for s in stocks:
#      print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

# ... look at the output ...
# >>>

# One thing to emphasize here is that the class Stock acts like a factory for
# creating instances of objects. Basically, you call it as a function and it
# creates a new object for you. Also, it must be emphasized that each object is
# distinct—they each have their own data that is separate from other objects
# that have been created.

# An object defined by a class is somewhat similar to a dictionary–just with
# somewhat different syntax. For example, instead of writing s['name'] or
# s['price'], you now write s.name and s.price.
#------------------------------------------------------------------------------

# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price


###############################################################################
# Exercise 4.2: Adding some Methods
# With classes, you can attach functions to your objects. These are known as
# methods and are functions that operate on the data stored inside an object.
# Add a cost() and sell() method to your Stock object. They should work like
# this:

# >>> import stock
# >>> s = stock.Stock('GOOG', 100, 490.10)
# >>> s.cost()
# 49010.0
# >>> s.shares
# 100
# >>> s.sell(25)
# >>> s.shares
# 75
# >>> s.cost()
# 36757.5
# >>>
#------------------------------------------------------------------------------

# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price

#     def sell(self, nshares):
#         self.shares -= nshares

#     def cost(self):
#         return self.shares * self.price


###############################################################################
# Exercise 4.9: Better output for printing objects
# Modify the Stock object that you defined in stock.py so that the __repr__()
# method produces more useful output. For example:

# >>> goog = Stock('GOOG', 100, 490.1)
# >>> goog
# Stock('GOOG', 100, 490.1)
# >>>

# See what happens when you read a portfolio of stocks and view the resulting
# list after you have made these changes. For example:

# >>> import report
# >>> portfolio = report.read_portfolio('Data/portfolio.csv')
# >>> portfolio
# ... see what the output is ...
# >>>
#------------------------------------------------------------------------------

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, nshares):
        self.shares -= nshares

    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares:d}, {self.price:.2f})"


###############################################################################
###############################################################################
