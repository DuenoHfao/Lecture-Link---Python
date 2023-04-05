import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import thefuzz
from thefuzz import fuzz
from thefuzz import process

def find_string(user_input, long_string, dict_array):
        fuzz.ratio(user_input, long_string)
        
    
def input_subject(user_input):
        subjects = ["Mathematics", "Chemistry", "Physics", "Economics", "General Paper"]
        subject_choice = process.extract(user_input, subjects, limit=1)
        print(subject_choice[0][0])
        return subject_choice