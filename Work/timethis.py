""" timethis.py
"""
###############################################################################
# Exercise 7.10: A decorator for timing
# If you define a function, its name and module are stored in the __name__ and
# __module__ attributes. For example:

# >>> def add(x,y):
#      return x+y

# >>> add.__name__
# 'add'
# >>> add.__module__
# '__main__'
# >>>

# In a file timethis.py, write a decorator function timethis(func) that wraps a
# function with an extra layer of logic that prints out how long it takes for a
# function to execute. To do this, you’ll surround the function with timing
# calls like this:

# start = time.time()
# r = func(*args,**kwargs)
# end = time.time()
# print('%s.%s: %f' % (func.__module__, func.__name__, end-start))

# Here is an example of how your decorator should work:

# >>> from timethis import timethis
# >>> @timethis
# def countdown(n):
#         while n > 0:
#              n -= 1

# >>> countdown(10000000)
# __main__.countdown : 0.076562
# >>>

# Discussion: This @timethis decorator can be placed in front of any function
# definition. Thus, you might use it as a diagnostic tool for performance
# tuning.
#------------------------------------------------------------------------------

from typing import Callable, Any
import time


def timethis(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end-start:f}')
        return res
    return wrapper


###############################################################################
###############################################################################
