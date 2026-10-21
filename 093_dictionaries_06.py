"""
Complete the get_student_grades() function that takes a single string parameter - filename - representing the name of the text file the function will read.

This text file consists of one or more lines of student data. Each line of student data consists of a name and an integer grade separated by a tab character. For example the student data:

Aina Krestel	18
is for a student named Aina Krestel who obtained a grade of 18. The name and the grade are separated by a tab character.

The function should read the text file and use the student data it contains to create a dictionary where:

The keys are strings representing student names.
The values are lists of integers representing their grades. The grades should be sorted in ascending order.
"""

def get_student_grades(filename):
    with open(filename, "r") as input_stream:
        grades_dict = {}
        
        line = input_stream.readline().strip()
        while line != "":
            line_list = line.split("\t")
            
            if line_list[0] in grades_dict:
                grades_dict[line_list[0]].append(int(line_list[1]))
                
            else:
                grades_dict[line_list[0]] = [int(line_list[1])]
                
            line = input_stream.readline().strip()
                
        for value in grades_dict.values():
            value.sort()
            
        return grades_dict

filename = "093_dictionaries_06_file.txt"
student_grades_dict = get_student_grades(filename)
for student in sorted(student_grades_dict):
    print(f"{student}: {student_grades_dict[student]}")
