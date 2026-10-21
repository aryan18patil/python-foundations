"""
Complete the print_invoice() function that takes 3 parameters:

1) transaction_tuple - This is a tuple object where each item is a tuple representing a transaction. The first item of a tuple object representing a transaction is the product ID of the
   product being purchased, while the second item is the number of units of this product being purchased. You can assume that the transaction_tuple will have at least 1 item (i.e., at
   least 1 tuple representing a transaction).
   
2) item_name_dict - This is a dictionary object such that each key-value pair is as follows:
   Key - A string representing a product ID.
   Value - A string representing the name of the product.
   
3) item_price_dict - This is a dictionary object such that each key-value pair is as follows:
   Key - A string representing a product ID.
   Value - A float representing the price of the product.

   
The function prints out an invoice summarizing the transactions specified by the transaction_tuple. The format of the invoice is as follows:

The title of the invoice is printed.

Each transaction is listed in the order they appear in the transaction_tuple. For each transaction, the format is as follows: product_name * units_purchased = $transaction_total. The
transaction total should be rounded to the nearest 2 decimal places.

A blank line is printed.

The overall invoice total is printed out. The format is as follows: Invoice Total: $invoice_total. The invoice total should be rounded to the nearest 2 decimal places.
"""

def print_invoice(transaction_tuple, item_name_dict, item_price_dict):
    print("Invoice\n=======")
    
    total = 0
    for item in transaction_tuple:
        price = item_price_dict[item[0]] * item[1]
        total += round(price, 2)
        
        print(
            f"{item_name_dict[item[0]]} * "
            f"{item[1]} = "
            f"${round(price, 2)}"
        )
        
    print(f"\nInvoice Total: ${total}")

transaction_tuple = (('A00001', 3), ('B00050', 2), ('A00103', 5), ("A00015", 2))
item_name_dict = {"A00001": "Snickers Chocolate Bar", "A00015": "Mars Chocolate Bar",
                  "A00103": "Bounty Chocolate Bar", "B00050": "Pams Standard Milk (1L)"}
item_price_dict = {"A00001": 1.25, "A00015": 1.35,
                  "A00103": 1.30, "B00050": 2.55}
print_invoice(transaction_tuple, item_name_dict, item_price_dict)
