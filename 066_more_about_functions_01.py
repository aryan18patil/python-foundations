"""
For this exercise you will need to complete 3 functions:

First complete the calculate_bmi() function that takes 2 parameters:

weight - an integer representing a person's weight in kilograms.
height - a floating point value representing the person's height in metres.
The function uses these parameters to calculate the person's body mass index (BMI) using the following formula: bmi = weight/height^2. The function then returns this value.

Next, complete the print_classification() function that takes a single floating point parameter, bmi. The function prints this bmi out to 2 decimal places and then uses it to print its
classification using the following criteria:

If a person's BMI is between 18.5 (inclusive) and 25.0 (not inclusive), the function should print "You have a healthy weight.".
If a person's BMI is 25.0 or more, the function should print "You may be overweight.".
If a person's BMI is below 18.5, the function should print "You may be underweight.".


Finally, complete the calculate_and_classify_bmi() function that takes 2 parameters:

weight - an integer representing a person's weight in kilograms.
height - a floating point value representing the person's height in metres.
The function first uses these 2 parameters when calling the calculate_bmi() function to calculate the person's BMI. It then uses this value when calling the print_classification()
function to print out a classification of their BMI.
"""

def calculate_and_classify_bmi(weight, height):
    print_classification(calculate_bmi(weight, height))

def calculate_bmi(weight, height):
    bmi = (weight) / (height ** 2)
    return bmi

def print_classification(bmi):
    print(f"You have a BMI of {round(bmi, 2)}")
    
    if 18.5 <= bmi < 25.0:
        print("You have a healthy weight.")
        
    elif bmi >= 25.0:
        print("You may be overweight.")
        
    else:
        print("You may be underweight.")

    print()

weight = 115
height = 1.83
calculate_and_classify_bmi(weight, height)

weight = 59
height = 1.73
calculate_and_classify_bmi(weight, height)

weight = 72
height = 2.03
calculate_and_classify_bmi(weight, height)
