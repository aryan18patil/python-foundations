"""
Complete the swap_elements() function that takes 2 tuples with integer elements as parameters: int_tuple1 and int_tuple2.

The function will return a tuple with 2 elements - both of which are tuples with integers. The returned tuples will contain the same integers as the parameter tuples, except where an
integer at index i of int_tuple1 is greater than the integer at index i of int_tuple2. In such a situation, the integers at this index are swapped in the returned tuples. For example
given these two integer tuples:

int_tuple1 = (6, 3, 5, 8)
int_tuple2 = (4, 7, 2, 9)


We can call the swap_elements() function passing it these two tuples as arguments. You can see that at indices 0 and 2, the integers in int_tuple1 are larger than the corresponding
integers in int_tuple2 (6 versus 4 and 5 versus 2 respectively). As such, in the returned tuples, we swap the values 6 and 4, so that 4 appears at index 0 of the first tuple and 6 appears
at index 0 of the second tuple. Similarly, we swap the values 5 and 2, so that 2 appears at index 2 of the first tuple and 5 appears at index 2 of the second tuple. This means that the
function will return:

((4, 3, 2, 8), (6, 7, 5, 9))


You can assume that the 2 parameter tuples will always have the same length.
"""

def swap_elements(int_tuple1, int_tuple2):
    numbers1 = list(int_tuple1)
    numbers2 = list(int_tuple2)
    
    for i in range(len(numbers1)):
        if numbers1[i] > numbers2[i]:
            numbers1[i], numbers2[i] = numbers2[i], numbers1[i]
            
    return (tuple(numbers1), tuple(numbers2))

number_tuple1 = (6, 18, 29, -4, 22, -3, 25, 19, -1, 6)
number_tuple2 = (2, 5, 5, -2, 24, 9, 16, 2, -9, 16)
number_tuple1, number_tuple2 = swap_elements(number_tuple1, number_tuple2)
print(f"Number Tuple 1 = {number_tuple1}")
print(f"Number Tuple 2 = {number_tuple2}")
