"""
CONCEPT (1):
Question: Calculate the estimated 2026 value of a house which was purchased in 1985 for $85,000 and has increased in value exponentially by a rate of 8% each year. The formula for
calculating the estimated value of a house after a certain number of years is:

Value of house = original_price * (1 + rate)^ number of years

Round the 2026 value of the house to a whole number of dollars.
"""

current_year = 2026
year_purchased = 1985
original_price = 85000
rate = 8 / 100

current_price = original_price * ((1 + rate) ** (current_year - year_purchased))

print(f"House is now worth approximately $ {round(current_price)}")
