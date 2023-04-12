import youtube_api
import fuzzy_search
import get_title
from youtube_api import *
from fuzzy_search import *
from get_title import *
import pandas as pd

user_input = input("Input subject name: ")
search_subject = input_subject(user_input)[0][0]

dataset = pd.read_csv("Lecture_dB.csv")
select_subj = dataset.loc[dataset["subject"] == search_subject]["link"]
# print(dataset)
# print(select_subj)
temp_title = []
for i in select_subj:
    temp_title.append(get_title(i))
    
print(temp_title)
