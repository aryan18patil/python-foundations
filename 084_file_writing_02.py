"""
Complete the write_student_data() function that takes 2 parameters:

filename - a string representing the name of a text file.
student_data_list - a list containing student data. Each item in this list is a tuple consisting of a string representing a student's name, and a floating point value representing their
grade. You can assume that this list will not be empty.

The function should write the student data in student_data_list to the text file specified by the filename. The format is as follows:

The first line should consist of the text "Student Grades".
The second line should consist of the text "--------------".
The third line should be blank.
The student data will be listed on the remaining lines, the data for one student per line. Each line will consist of the name of a student, followed by ": " followed by their grade. The
students should be listed in ascending order.


Note:

Remember to close the file.
"""

def write_student_data(filename, student_data_list):
    sorted_student_data_list = sorted(student_data_list)
    intro = "Student Grades\n--------------\n\n"
    
    with open(filename, "w") as output_stream:
        output_stream.write(intro)
        
        for data in sorted_student_data_list:
            profile = f"{data[0]}: {data[1]}\n"
            output_stream.write(profile)

def print_contents(filename):
    with open(filename, 'r') as input_file:
        content = input_file.read()
    print(content)

filename = '084_file_writing_02_file.txt'
student_data_list = [("Zach", 52.9), ("Katie", 68.5), ("Becky", 71.3),
                     ("Roger", 47.2)]
write_student_data(filename, student_data_list)
print_contents(filename)
