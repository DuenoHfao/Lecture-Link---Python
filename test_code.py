import sys
import os
import random
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
import thefuzz
from thefuzz import fuzz

os.system('cls')
arr = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(arr)
full_text = ""
for v in arr:
    full_text += v + " "
    
ratio = {"Ratio": fuzz.ratio("brown fox", full_text),
             "Partial": fuzz.partial_ratio("brown fox", full_text),
             "Token Sort": fuzz.token_sort_ratio("brown fox", full_text),
             "Token Set": fuzz.token_set_ratio("brown fox", full_text)
             }
print(ratio, end="\n \n")        

for i in range(5):
    random.shuffle(arr)
    print(arr)
    full_text = ""
    for v in arr:
        full_text += v + " "
        
    ratio = {"Ratio": fuzz.ratio("brown fox", full_text),
             "Partial": fuzz.partial_ratio("brown fox", full_text),
             "Token Sort": fuzz.token_sort_ratio("brown fox", full_text),
             "Token Set": fuzz.token_set_ratio("brown fox", full_text)
             }
    print(ratio, end="\n \n")