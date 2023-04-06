import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import thefuzz
from thefuzz import fuzz
from thefuzz import process

user_input = "k multiplier process"
long_string = "Okay today we will be covering national income in a graph. To determine the national income, we will need to be able to determine change in AD, multiplied by the k process. To determine the k process, we will need to make several assumptions and..."

ratio = {"Ratio": fuzz.ratio(user_input, long_string),
        "Partial": fuzz.partial_ratio(user_input, long_string),
        "Token Sort": fuzz.token_sort_ratio(user_input, long_string),
        "Token Set": fuzz.token_set_ratio(user_input, long_string)
        }
print(ratio)
input_break = user_input.split(" ")
ls_break = long_string.split(" ")
temp_corr = []
for item in input_break:
    item = process.extractOne(item, ls_break, scorer=fuzz.token_set_ratio)[0]
    temp_corr.append(item)

print(temp_corr)