"""
Complete the process_barchart() function that takes a single string parameter, filename. This parameter specifies the name of the text file that the function will open and read the
contents from.

The text files processed by the function will each contain a letter frequency bar chart. Each line in the text file will be a row in the letter frequency bar chart. A row consists of a
letter, followed by the "|" character, followed by a sequence of "#" characters. The number of "#" characters indicates the letter frequency.

The process_barchart() function will use the bar chart to create and return a tuple containing the letter frequencies found in the chart. Each item in the tuple will be a tuple with 2
items: a letter and its corresponding frequency. Note: you must close the file once you have read its contents.
"""

def process_barchart(filename):
    with open(filename, "r") as input_stream:
        line = input_stream.readline().strip()
        frequency_list = []
        
        while line != "":
            line_list = line.split("|")
            frequency_list.append((line_list[0], len(line_list[1])))
            line = input_stream.readline().strip()
            
    return tuple(frequency_list)

filename = "barchart1.txt"
print(f"Letter frequencies from {filename}: {process_barchart(filename)}")
