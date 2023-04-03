import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import thefuzz
from thefuzz import fuzz
from thefuzz import process

search_string = "no gratification"
test_case = '''Such is the rabbit hole of the internet, yet we keep coming back for the instant gratification.'''
string_array = ["Instant gratification", "No gratification", "Lack of gratitude", "No gratitude"]
ratio = {"Simple": fuzz.ratio(search_string, test_case), 
         "Partial": fuzz.partial_ratio(search_string, test_case),
         "Token Sort": fuzz.token_sort_ratio(search_string, test_case),
         "Token Set": fuzz.token_set_ratio(search_string, test_case)
         }

for items in ratio:
    print(f"{items:10}: {ratio[items]}")

generic_scoring = process.extract(search_string, string_array, limit=2)
print(generic_scoring)