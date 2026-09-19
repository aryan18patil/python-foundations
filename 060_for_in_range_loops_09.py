"""
Run Length Encoding (RLE) is a compression technique where values repeated in sequence are counted and stored as the value and its count. We will consider a simple version of RLE that will
be applied to strings. Given a string, this version of RLE encoding will produce a new string where any characters repeated in sequence are represented by that character and its count.
Characters that are not repeated in sequence remain unchanged. Therefore, the string "Baaaad" would be encoded as "Ba4d". Similarly, the string "Nooo" would be encoded as "No3".

Complete the run_length_encoding() function that takes a single string parameter text. The function returns the resulting RLE encoded string using the guidelines discussed previously. You
can assume that text will only contain alphabetical characters and have a length of at least 1.
"""

def run_length_encoding(text):
    encoded_text = text[0]
    repeat_count = 1
    
    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            repeat_count += 1
            
        elif text[index] != text[index - 1]:
            if repeat_count == 1:
                encoded_text += text[index]
                
            else:
                encoded_text += f"{repeat_count}{text[index]}"
                repeat_count = 1
                
    if repeat_count != 1:
        encoded_text += str(repeat_count)
                
    return encoded_text

text = "mississippi"
encoded_text = run_length_encoding(text)
print(text, "--->", encoded_text)

text = "DdAAABBBBBccccc"
encoded_text = run_length_encoding(text)
print(text, "--->", encoded_text)
