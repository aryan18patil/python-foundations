"""
Complete the get_string_distance() function that takes two string parameters, string1 and string2. The function returns the "distance" between the two strings. In other words, the number
of characters by which they differ. For example, the strings "Ann" and "Anya" have a distance of 2. They differ in terms of the character at index 2 ("n" in Ann and "y" in Anya") and by
the fact that "Anya" has an additional character (the last character "a").
"""

def get_string_distance(string1, string2):
    diff_count = abs(len(string1) - len(string2))
        
    for index in range(min(len(string2), len(string1))):
        if string1[index] != string2[index]:
            diff_count += 1
                
    return diff_count

string1 = "Ann"
string2 = "Anya"
print("Distance between", string1, "and", string2, "is:", get_string_distance(string1, string2))
