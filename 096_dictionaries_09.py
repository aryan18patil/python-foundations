"""
Complete the process_marks(filename) function that takes a string parameter, a filename, processes the data within the specified file, and returns a dictionary containing this data.

Each line of the file has the following format:
name1,name2,name3,...,nameN,mark1:mark2:mark3:...:markN

You can see that each line consists of a comma-separated list of items: N names followed by a collection of N marks. Each of the marks is separated by a colon ":".

You can assume that there will always be the same number of names and marks, and that there is a one-to-one correspondence between names and marks. Therefore, name1 and mark1 are a pair,
name2 and mark2 are a pair and so on.

The process_marks() function should process the file containing lines of data in the above format and return a dictionary where the keys are names (strings), and the values are tuples of
the associated marks (integers). The marks in the tuples should be sorted in ascending order (from smallest to largest).
"""

def process_marks(filename):
    with open(filename, "r") as input_stream:
        marks_dict = {}
        
        line = input_stream.readline().strip()
        while line != "":
            digit = False
            i = 0
            while not digit:
                if line[i].isdigit():
                    digit_index = i
                    digit = True
                    
                i += 1
                
            names_list = line[:(digit_index - 1)].split(",")
            marks_list = line[digit_index::].split(":")
            
            for i in range(len(names_list)):
                if names_list[i] in marks_dict:
                    marks_dict[names_list[i]].append(int(marks_list[i]))
                    
                else:
                    marks_dict[names_list[i]] = [int(marks_list[i])]
                    
            line = input_stream.readline().strip()
            
        for key, value in marks_dict.items():
            value.sort()
            marks_dict[key] = tuple(value)
            
        return marks_dict

def print_dict(a_dict):
    key_list = list(a_dict.keys())
    key_list.sort()
    for key in key_list:
        print(str(key )+ ": " + str(a_dict[key]))

filename1 = "096_dictionaries_09_file.txt"
marks_dict = process_marks(filename1)
print_dict(marks_dict)
