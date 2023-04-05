import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import thefuzz
from thefuzz import fuzz
from thefuzz import process

def find_string(user_input, long_string, dict_array):
    ratio = {"Simple": fuzz.ratio(user_input, long_string), 
            "Partial": fuzz.partial_ratio(user_input, long_string),
            "Token Sort": fuzz.token_sort_ratio(user_input, long_string),
            "Token Set": fuzz.token_set_ratio(user_input, long_string)
            }
    indv_input_words = user_input.split(" ")
    return
    
def input_subject(user_input):
        subjects = ["Mathematics", "Chemistry", "Physics", "Economics", "General Paper"]
        subject_choice = process.extract(user_input, subjects, limit=1)
        print(subject_choice)
        return subject_choice