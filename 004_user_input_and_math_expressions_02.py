"""
You are a painter who charges for their services based on the area of the surface to be painted. Write a program that asks the user for the length and width of a room and calculates the
cost of painting it based on the following pricing scheme:

Walls cost $25 per square metre to paint.
Ceilings cost $30 per square metre to paint.
Assume that the room is 2.4 metres high.
Your program should display the total cost of painting the room, including 4 walls and ceiling, but not the floor (assume the floor has carpet).


Notes:

Round your answer to the nearest dollar.
The user may enter the lengths as integer values or floating point values.
"""

height = 2.4
length = float(input("Enter the length of the room in metres: "))
width = float(input("Enter the width of the room in metres: "))

cost_walls = 25 * ((2 * length * height) + (2 * width * height))
cost_ceiling = 30 * (length * width)
total_cost = cost_walls + cost_ceiling

print(f"The total cost is ${round(total_cost)}")
