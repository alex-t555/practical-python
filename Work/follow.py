""" follow.py
"""
###############################################################################
# Exercise 6.5: Monitoring a streaming data source
# Generators can be an interesting way to monitor real-time data sources such as log files or stock market feeds. In this part, we’ll explore this idea. To start, follow the next instructions carefully.

# The program Data/stocksim.py is a program that simulates stock market data. As output, the program constantly writes real-time data to a file Data/stocklog.csv. In a separate command window go into the Data/ directory and run this program:

# bash % python3 stocksim.py
# If you are on Windows, just locate the stocksim.py program and double-click on it to run it. Now, forget about this program (just let it run). Using another window, look at the file Data/stocklog.csv being written by the simulator. You should see new lines of text being added to the file every few seconds. Again, just let this program run in the background—it will run for several hours (you shouldn’t need to worry about it).

# Once the above program is running, let’s write a little program to open the file, seek to the end, and watch for new output. Create a file follow.py and put this code in it:

# # follow.py
# import os
# import time

# f = open('Data/stocklog.csv')
# f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1)   # Sleep briefly and retry
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

# If you run the program, you’ll see a real-time stock ticker. Under the hood,
# this code is kind of like the Unix tail -f command that’s used to watch a log
# file.

# Note: The use of the readline() method in this example is somewhat unusual in
# that it is not the usual way of reading lines from a file (normally you would
# just use a for-loop). However, in this case, we are using it to repeatedly
# probe the end of the file to see if more data has been added (readline() will
# either return new data or an empty string).
#------------------------------------------------------------------------------

# import os
# import time


# BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
# FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

# with open(FILE_STOCKLOG) as f:
#     f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

#     while True:
#         line = f.readline()
#         if line == '':
#             time.sleep(0.1)   # Sleep briefly and retry
#             continue
#         fields = line.strip().split(',')
#         name = fields[0].strip('"')
#         price = float(fields[1])
#         change = float(fields[4])
#         if change < 0:
#             print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


###############################################################################
# Exercise 6.6: Using a generator to produce data
# If you look at the code in Exercise 6.5, the first part of the code is
# producing lines of data whereas the statements at the end of the while loop
# are consuming the data. A major feature of generator functions is that you
# can move all of the data production code into a reusable function.

# Modify the code in Exercise 6.5 so that the file-reading is performed by a
# generator function follow(filename). Make it so the following code works:

# >>> for line in follow('Data/stocklog.csv'):
#           print(line, end='')

# ... Should see lines of output produced here ...
# Modify the stock ticker code so that it looks like this:

# if __name__ == '__main__':
#     for line in follow('Data/stocklog.csv'):
#         fields = line.split(',')
#         name = fields[0].strip('"')
#         price = float(fields[1])
#         change = float(fields[4])
#         if change < 0:
#             print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
#------------------------------------------------------------------------------

# from typing import Generator
# import os
# import time


# def follow(filename: str) -> Generator[str, None, None]:
#     with open(filename) as f:
#         f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
#         while True:
#             line_ = f.readline()
#             if line_ == '':
#                 time.sleep(0.1)   # Sleep briefly and retry
#                 continue
#             yield line_


# if __name__ == '__main__':

#     BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
#     FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

#     for line in follow(FILE_STOCKLOG):
#         fields = line.strip().split(',')
#         name = fields[0].strip('"')
#         price = float(fields[1])
#         change = float(fields[4])
#         if change < 0:
#             print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


###############################################################################
# Exercise 6.7: Watching your portfolio
# Modify the follow.py program so that it watches the stream of stock data and
# prints a ticker showing information for only those stocks in a portfolio. For
# example:

# if __name__ == '__main__':
#     import report

#     portfolio = report.read_portfolio('Data/portfolio.csv')

#     for line in follow('Data/stocklog.csv'):
#         fields = line.split(',')
#         name = fields[0].strip('"')
#         price = float(fields[1])
#         change = float(fields[4])
#         if name in portfolio:
#             print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

# Note: For this to work, your Portfolio class must support the in operator.
# See Exercise 6.3 and make sure you implement the __contains__() operator.
#------------------------------------------------------------------------------

from typing import Generator
import os
import time


def follow(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
        while True:
            line_ = f.readline()
            if line_ == '':
                time.sleep(0.1)   # Sleep briefly and retry
                continue
            yield line_


if __name__ == '__main__':

    import report

    BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
    FILE_PORTFOLIO = BASE + 'Data/portfolio.csv'
    FILE_STOCKLOG = BASE + 'Data/stocklog.csv'

    portfolio = report.read_portfolio(FILE_PORTFOLIO)

    for line in follow(FILE_STOCKLOG):
        fields = line.strip().split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


###############################################################################
###############################################################################
