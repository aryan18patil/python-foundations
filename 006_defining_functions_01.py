"""
To calculate a fixed monthly loan payment, use the standard loan formula below:
 
M = P × ((r (1 + r) ^ n) / ((1 + r) ^ n − 1))


Notes:

M is the monthly payment
P is the principal loan amount (i.e., the starting balance)
r is the monthly interest rate. To get the monthly interest rate, divide the annual interest rate by 12.
n is the number of months for the loan (e.g., for a 3 year loan, n = 3 x 12 = 36)


Write a function called loan_repayments() that accepts principal in dollars (int), annual_interest_rate (float), and duration in months (int). The function should return the monthly
payments as a float, rounded to the nearest cent. Include a docstring describing the function.
"""

def loan_repayments(principal, annual_interest_rate, duration):
    """
Calculates loan repayments

principal - amount borrowed (int)
annual_interest_rate - interest rate as a decimal (e.g., 4% is 0.04) (float)
duration - loan duration in months (int)

return - repayment amount to 2 decimal places (float)
    """

    monthly_payment = principal * (((annual_interest_rate / 12) * ((1 + (annual_interest_rate / 12)) ** duration)) / (((1 + (annual_interest_rate / 12)) ** duration) - 1))

    return f"{monthly_payment:.2f}"
