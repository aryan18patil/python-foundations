"""
For this exercise you will need to complete 3 functions:

First complete the get_discounted_price() function that takes 2 parameters:

price - a floating point value representing an item's price.
discount - an integer value representing the percentage discount.
The function uses these parameters to calculate the discounted price using the following formula: discounted price=price∗((100−discount)/100)
. The function then returns this value.

Next, complete the print_discount_details() function that takes a 3 parameters:

price - a floating point value representing an item's price.
discount - an integer value representing the percentage discount.
discounted_price - a floating point value representing the discounted price obtained when applying the discount on the price.
The function should print out the details of the discount in the format: "${price} after a {discount}% discount is ${discounted price}." Note that the discounted_price should be printed
to 2 decimal places.

Finally, complete the discount_calculator() function that takes takes 2 parameters:

price - a floating point value representing am item's price.
discount - an integer value representing the percentage discount.
The function first uses these 2 parameters when calling the get_discounted_price() function to calculate the discounted price. It then uses this value along with the 2 parameters when
calling the print_discount_details() function to print out the details of the discount.
"""

def discount_calculator(price, discount):
    print_discount_details(
        price, discount, get_discounted_price(price, discount)
    )

def get_discounted_price(price, discount):
    return (price * ((100 - discount) / 100))

def print_discount_details(price, discount, discounted_price):
    print(
        f"${price} after a {discount}% discount is"
        f" ${discounted_price:.2f}."
    )
    print()

price = 82.99
discount = 20
discount_calculator(price, discount)

price = 699.49
discount = 30
discount_calculator(price, discount)
