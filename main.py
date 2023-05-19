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
select_subj_link = dataset.loc[dataset["subject"] == search_subject]["link"]
# print(dataset)
# print(select_subj_link)
temp_title = []
for i in select_subj_link:
    temp_title.append(get_title(i)[0])
    
transcript = ''' '''
for link in select_subj_link:
    transcript = get_transcript(link)[1]
    user_input = input("Enter keyword: ")
    corrolate_text = find_string(user_input, transcript, full_text)
    