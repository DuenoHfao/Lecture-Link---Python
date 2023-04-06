import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import thefuzz
from thefuzz import fuzz
from thefuzz import process

def find_string(user_input, long_string, full_text):
        ratio = {"Ratio": fuzz.ratio(user_input, long_string),
             "Partial": fuzz.partial_ratio(user_input, long_string),
             "Token Sort": fuzz.token_sort_ratio(user_input, long_string),
             "Token Set": fuzz.token_set_ratio(user_input, long_string)
             }
        input_break = user_input.split(" ")
        ls_break = long_string.split(" ")
        temp_corr = []
        for item in input_break:
                item = process.extractOne(item, ls_break, scorer=fuzz.token_set_ratio)[0]
                temp_corr.append(item)

        to_return = []
        for find_text in full_text:
                for i in temp_corr:
                        if find_text[0] == i:
                                to_return.append(find_text["start"])
        return to_return

    
def input_subject(user_input):
        subjects = ["Mathematics", "Chemistry", "Physics", "Economics", "General Paper"]
        subject_choice = process.extract(user_input, subjects, limit=1)
        print(subject_choice[0][0])
        return subject_choice