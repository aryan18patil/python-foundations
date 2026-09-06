"""
Write a program which prompts the user to answer a few questions in order to calculate the fee a patient has to pay when they visit an Urgent Care Clinic. The table below shows the fees:

0-5 years	$30.00
6-13 years, card holder	$60.00
6-13 years, non-card holder	$65.00
14-17 years, card holder	$60.00
14-17 years, non-card holder	$65.00
18-64 years, card holder	$80.00
18-64 years, non-card holder	$95.00
65+ years, card holder	$80.00
65+ years, non-card holder	$95.00
"""

age = int(input("Enter your age: "))
card_status = input("Are you a card holder? ('Y' for yes): ")

if card_status == "Y":
    if 0 <= age <= 5:
        fee = 30
        
    elif 6 <= age <= 17:
        fee = 60
        
    elif age >= 18:
        fee = 80
        
else:
    if 0 <= age <= 5:
        fee = 30
        
    elif 6 <= age <= 17:
        fee = 65
        
    elif age >= 18:
        fee = 95
        
print(f"The payment is ${fee}")
