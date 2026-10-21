"""
Complete the merge_staff_dictionaries() function which takes two dictionary objects as parameters:

name_upi_dict - a dictionary where the keys are the names of university staff and the values are their usernames (also referred to as upis). The keys and values are strings.
upi_id_dict - a dictionary where the keys are the upis of university staff and the values are their staff id numbers. The keys and values are strings.

The function creates and returns a new dictionary where a key is a staff member's name and the associated value is a tuple containing their upi and staff id number (in that order). You
can assume that the values (upis) in name_upi_dict are keys in upi_id_dict.
"""

def merge_staff_dictionaries(name_upi_dict, upi_id_dict):
    new_dict = {}
    
    for name, upi in name_upi_dict.items():
        new_dict[name] = (upi, upi_id_dict[upi])
        
    return new_dict

name_upi_dict = {"Damir":"dazh001", "Ann":"acam001"}
upi_id_dict = {'dazh001':"1234567", "acam001":"7654321"}
staff_details_dict = merge_staff_dictionaries(name_upi_dict, upi_id_dict)
for key in sorted(staff_details_dict):
    print(key, staff_details_dict[key])
print(type(staff_details_dict))
print()

name_upi_dict = {"Damir":"dazh001", "Ann":"acam001", "Andrew":"alux001", "Angela":"acha001"}
upi_id_dict = {'dazh001':"1234567", "alux001":"1112223", "acam001":"7654321", "acha001":"5566771"}
staff_details_dict = merge_staff_dictionaries(name_upi_dict, upi_id_dict)
for key in sorted(staff_details_dict):
    print(key, staff_details_dict[key])
print()
