"""
Write a function called triangle_type() that accepts the length of three triangle sides as parameters: a, b and c. The function should return the triangle category (string), or "None" if
the triangle does not exist.

The triangle does not exist if the length of a side is greater than or equal to the sum of the other sides
The triangle category is "Equilateral" when all three sides are the same length
The triangle category is "Isosceles" when exactly two sides are equal length
In all other cases, the triangle category is Obtuse
"""

def triangle_type(a, b, c):
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        category = "None"

    elif a == b == c:
        category = "Equilateral"

    elif (a == b) or (b == c) or (a == c):
        category = "Isosceles"

    else:
        category = "Obtuse"

    return category
