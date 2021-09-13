""" mortgage.py
"""

W = 79

###############################################################################
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with
# Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The
# interest rate is 5% and the monthly payment is $2684.11.

# Here is a program that calculates the total amount that Dave will have to pay
# over the life of the mortgage:

# Enter this program and run it. You should get an answer of 966,279.6.
#------------------------------------------------------------------------------

exercise = "Module 1.3 / Exercise 1.7"
print("", "#"*W, f"{exercise:^{W:d}s}", "-"*W, sep="\n")

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid:', round(total_paid, 2))


###############################################################################
# Exercise 1.8: Extra payments
# Suppose Dave pays an extra $1000/month for the first 12 months of the
# mortgage?

# Modify the program to incorporate this extra payment and have it print the
# total amount paid along with the number of months required.

# When you run the new program, it should report a total payment of 929,965.62
# over 342 months.
#------------------------------------------------------------------------------

exercise = "Module 1.3 / Exercise 1.8"
print("", "#"*W, f"{exercise:^{W:d}s}", "-"*W, sep="\n")

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
total_mounth = 0

while principal > 0:
    total_mounth += 1
    if total_mounth <= 12:
        pay = payment + extra_payment
    else:
        pay = payment
    principal = principal * (1+rate/12) - pay
    total_paid += pay

print('Total paid:', round(total_paid, 2), total_mounth)


###############################################################################
# Exercise 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally
# handled. Make it so that the user can set these variables:

    # extra_payment_start_month = 61
    # extra_payment_end_month = 108
    # extra_payment = 1000

# Make the program look at these variables and calculate the total paid
# appropriately.

# How much will Dave pay if he pays an extra $1000/month for 4 years starting
# after the first five years have already been paid?
#------------------------------------------------------------------------------

exercise = "Module 1.3 / Exercise 1.9"
print("", "#"*W, f"{exercise:^{W:d}s}", "-"*W, sep="\n")

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
total_mounth = 0

while principal > 0:
    total_mounth += 1
    if extra_payment_start_month <= total_mounth <= extra_payment_end_month:
        pay = payment + extra_payment
    else:
        pay = payment
    principal = principal * (1+rate/12) - pay
    total_paid += pay

print('Total paid:', round(total_paid, 2), total_mounth)


###############################################################################
# Exercise 1.10: Making a table
# Modify the program to print out a table showing the month, total paid so far,
# and the remaining principal. The output should look something like this:

#     1 2684.11 499399.22
#     2 5368.22 498795.94
#     3 8052.33 498190.15
#     4 10736.44 497581.83
#     5 13420.55 496970.98
#     ...
#     308 874705.88 3478.83
#     309 877389.99 809.21
#     310 880074.1 -1871.53
#     Total paid 880074.1
#     Months 310
#------------------------------------------------------------------------------

exercise = "Module 1.3 / Exercise 1.10"
print("", "#"*W, f"{exercise:^{W:d}s}", "-"*W, sep="\n")

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
total_mounth = 0

while principal > 0:
    total_mounth += 1
    if extra_payment_start_month <= total_mounth <= extra_payment_end_month:
        pay = payment + extra_payment
    else:
        pay = payment
    principal = principal * (1+rate/12) - pay
    total_paid += pay
    print(total_mounth, round(total_paid, 2), round(principal, 2))


###############################################################################
# Exercise 1.11: Bonus
# While you’re at it, fix the program to correct for the overpayment that
# occurs in the last month.
#------------------------------------------------------------------------------

exercise = "Module 1.3 / Exercise 1.11"
print("", "#"*W, f"{exercise:^{W:d}s}", "-"*W, sep="\n")

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
total_mounth = 0

while principal > 0:
    total_mounth += 1
    if extra_payment_start_month <= total_mounth <= extra_payment_end_month:
        pay = payment + extra_payment
    else:
        pay = payment
    principal = principal * (1+rate/12) - pay
    principal = max(principal, 0)
    total_paid += pay
    print(total_mounth, round(total_paid, 2), round(principal, 2))


###############################################################################
