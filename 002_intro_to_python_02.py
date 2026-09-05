"""
CONCEPT (1):
Question: From the moment a driver spots a potentially dangerous situation, to the moment when the car comes to a complete stop, it travels a certain distance. Given a friction
coefficient 'f', a perception coefficient 'p', and a distance factor 'd', the formula to calculate the stopping distance is:

stopping distance = (p ∗ time ∗ speed) + ((speed ^ 2) / (d ∗ f))


Write a program that, given the speed and reaction time, displays the stopping distance that your car travels after you hit the brakes. Assume that:

friction coefficient 'f' is 0.7 
perception coefficient 'p' is 0.278
distance factor 'd' is 254

For example, given the following initial values:

speed = 60
reaction_time = 1.5

the program should produce the following output:

"The stopping distance is 45.27 metres."


Please note the following:

The stopping distance should be rounded to the nearest 2 decimal places.
"""

speed = 60
reaction_time = 1.5
friction_coefficient = 0.7 
perception_coefficient = 0.278
distance_factor = 254

stopping_distance = (
    (perception_coefficient * reaction_time * speed)
    + ((speed ** 2) / (distance_factor * friction_coefficient))
)

print(f"The stopping distance is {round(stopping_distance, 2)} metres.")
