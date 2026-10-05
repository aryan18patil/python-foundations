"""
Complete the get_line_averages() function that takes a single string parameter - filename - which specifies the text file the function will read. The text file will consist of lines of
floating point values, where the values in each line are separated by one or more spaces. The function reads the contents of the text file and returns a list containing the average values
of each line in the text file. As such, the first item in the list will be the average of the values in the first line of the text file, the second item in the list will be the average of
the values in the second line of the text file, and so on. You can assume that each line will have at least one floating point value. Do not round the averages.
"""

def get_line_averages(filename):
    with open(filename, "r") as input_stream:
        line = input_stream.readline().strip()
        avg_list = []
        
        while line != "":
            line_list = line.split()
            line_sum = 0
            for n in line_list:
                line_sum += float(n)
                
            line_avg = line_sum / len(line_list)
            avg_list.append(line_avg)
            
            line = input_stream.readline().strip()
            
    return avg_list

filename = "078_file_reading_01_InputFile1.txt"
line_averages = get_line_averages(filename)
for i in range(len(line_averages)):
    print(f"{i + 1}. Average = {line_averages[i]:.2f}")
