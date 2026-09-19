"""
Complete the rotate_text() function that takes 2 parameters, a string data and an integer n. 

If n is positive, then the function will shift all the characters in data forward by n positions, with characters at the end of the string being moved to the start of the string. If n is
0 then the text remains the same.

For example:

rotate_text('abcde', 1) would return the string 'eabcd'
rotate_text('abcde', 3) would return the string 'cdeab'
rotate_text('abcde', 5) would return the string 'abcde'
rotate_text('abcde', 6) would return the string 'eabcd'

... and so on.

If n is negative, then the function will shift the characters in data backward by n positions, with characters at the start of the string being moved to the end of the string.

For example:

rotate_text('abcde', -1) would return the string 'bcdea'
rotate_text('abcde', -3) would return the string 'deabc'
rotate_text('abcde', -5) would return the string 'abcde'
rotate_text('abcde', -6) would return the string 'bcdea'

... and so on.


Note:
You can assume that the data string contains at least one character.
You MUST use for in range loop, and you MUST NOT use string slicing.
"""

def rotate_text(data, n):
    if (n == 0) or (len(data) == 1) or (abs(n) == len(data)):
        output = data
        
    elif n > 0:
        count = 0
        
        part2 = ""
        for index in range((len(data)) - (n % len(data))):
            part2 += data[index]
            count += 1
            
        part1 = ""
        for index in range(count, len(data)):
            part1 += data[index]
            
        output = part1 + part2
        
    else:
        count = 0
        
        part2 = ""
        for index in range(abs(n) % len(data)):
            part2 += data[index]
            count += 1
            
        part1 = ""
        for index in range(count, len(data)):
            part1 += data[index]
            
        output = part1 + part2
        
    return output

result = rotate_text('Hello', 1)
print(result)

result = rotate_text('Hello_World', -5)
print(result)
