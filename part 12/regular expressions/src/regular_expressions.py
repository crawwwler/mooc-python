# Write your solution here
import re
def is_dotw(my_string: str):
    ex = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(ex, my_string):
        return True
    return False

def all_vowels(my_string: str):
    ex = "^[aeiou]+$"
    if re.search(ex,my_string):
        return True
    return False

def time_of_day(my_string: str):
    ex = "[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}"
    exalt = "[0-2]{1}[0-3]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}"
    if my_string[0] == "2":
        if re.search(exalt, my_string):
            return True
    else :
        if re.search(ex, my_string):
            return True
        
    return False