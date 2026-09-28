"""
Complete the print_invoice() function that takes 3 parameters:

items - a tuple of strings representing the names of the items bought.
prices - a tuple of floats representing the prices of the items bought.
units_bought - a tuple of integers representing the number of units of each item bought.

You can assume that there is a one-to-one correspondence between the 3 tuples. The item at index i of items represents the name of an item purchased, the item at index i of prices,
represents its price (for a single unit), and the item at index i of units_bought represents the number of units bought.

The function will use this data to print an invoice for the purchase. The invoice will consist of a header, followed by a blank line, followed by a numbered list of the items bought and
their cost, followed by a blank line, followed by the total cost of the purchase. Each line of the list will have the following format:
{item number}. {name of item} * {number of units bought} = ${cost of purchasing this many units of the item}
"""

def print_invoice(items, prices, units_bought):
    print("Order Invoice")
    print("-------------")
    print()
    
    total_price = 0
    
    for i in range(len(items)):
        total_item_price = units_bought[i] * prices[i]
        
        print(
            f"{i + 1}. {items[i]} * {units_bought[i]} = "
            f"${total_item_price:.1f}"
        )
        
        total_price += total_item_price
        
    print()
    print(f"Total Price: ${total_price:.1f}")

items = ("Snickers Chocolate Bar", "Crunchie Chocolate Bar", "Whittakers Peanut Slab")
prices = (2.5, 1.5, 2.1)
units_bought = (3, 5, 4)
print_invoice(items, prices, units_bought)

items = ("Tip Top Trumpet", "Magnum Almond", "Magnum Classic", "Kapiti White Chocolate & Berry")
prices = (9.4, 11.0, 11.0, 11.5)
units_bought = (5, 6, 3, 4)
print_invoice(items, prices, units_bought)
