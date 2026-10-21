"""
Complete the get_max_keys() function that takes a dictionary object, data_dict, as a parameter. The parameter contains string keys and integer values. The get_max_keys() function returns
a tuple of keys that have the largest integer value. The keys in this tuple should be sorted in ascending order (smallest to largest/A-Z). Note that if data_dict is empty, the
get_max_keys() function returns an empty tuple.
"""

def get_max_keys(data_dict):
    max_list = []
    
    values_list = list(data_dict.values())
    
    if len(values_list) > 0:
        max_value = max(values_list)
    
        for key, value in data_dict.items():
            if value == max_value:
                max_list.append(key)
            
        max_list.sort()
    
    return tuple(max_list)

data_dict = {"cat":9001,"hello":24,"a":413,"world":-1,"dog":9001}
print(get_max_keys(data_dict))
print()

data_dict = {}
print(get_max_keys(data_dict))
print()
