"""
Complete the get_grade_summary() function that takes a single string parameter - filename - specifying the name of the text file the function will read. Each line of the text file contains
a student's grades formatted as follows:

Student_ID  Student_Surname  Student_First_Name  Grade1  Grade2  Grade3
Each item of student data is separated by a tab character '\t'. You can assume that the text file will contain data for at least 1 student.

The function should return a list of tuples summarizing the students' grades. Each tuple will consist of two elements:

The name of the student. This will consist of the student's first name, followed by a single space character, followed by their surname.
Their average grade.
The list should be sorted in alphabetical order based on the students' names.
"""

def get_grade_summary(filename):
    with open(filename, "r") as input_stream:
        line = input_stream.readline().strip()
        marks_list = []
        
        while line != "":
            line_list = line.split("\t")
            
            sum = int(line_list[3]) + int(line_list[4]) + int(line_list[5])
            avg = sum / 3
            
            marks_list.append((f"{line_list[2]} {line_list[1]}", avg))
            
            line = input_stream.readline().strip()
            
    marks_list.sort()
    
    return marks_list

filename = "082_file_reading_05_Grades1.txt"
grade_summary = get_grade_summary(filename)
print(type(grade_summary))
for student in grade_summary:
    print(f"{type(student)} {type(student[0])} {type(student[1])}")

filename = "082_file_reading_05_Grades1.txt"
grade_summary = get_grade_summary(filename)
for student in grade_summary:
    print(f"Average mark for {student[0]} = {student[1]:.1f}")
