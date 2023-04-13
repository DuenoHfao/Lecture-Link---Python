import sys
# sys.path.append( 'C:\Users\jeant\AppData\Local\Programs\Python\Python310\Lib\site-packages\thefuzz' )
sys.path.append( '../../../../AppData/Local/Programs/Python/Python310/Lib/site-packages/' )
# for path in sys.path:
#     print(path)

import math
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
                                to_return.append(int(find_text["start"]))
        return to_return

    
def input_subject(user_input):
        subjects = ["Mathematics", "Chemistry", "Physics", "Economics", "General Paper"]
        subject_choice = process.extract(user_input, subjects, limit=1)
        print(subject_choice[0][0])
        return subject_choice

def find_topic(user_input, subject):
        topics = {
                "Physics": [],
                "Chemistry": ["Atomic Structure", "Atoms, Molecules and Stoichiometry & Redox", "Chemical Bonding", "The Gaseous State", "Chemical Energetics I", "Chemical Energetics II", "Reaction Kinetics", "Chemical Equilibria", "Solubility Equilibria", "Introduction to Organic Chemistry", "Alkanes", "Alkenes", "Arenes", "The Periodic Table", "Theories of Acids and Bases", "Halogen Derivatives", "Hydroxy Compounds", "Carbonyl Compounds", "Carboxylic Acids and Derivatives", "Nitrogen Compounds", "Electrochemistry", "Electrolytic Cell", "Transition Element", "Galvanic Cell"],
                "Mathematics": [],
                "Economics": ["Central Economic Problem", "Basics of Market Economy", "Market Economy", "Elasticity Concepts", "Market Failure", "Equity", "Firms and Decisions", "Cost of Production", "Market Structure", "Decisions and Strategies of Firms", "Introduction to Macroeconomics", "National Income Accounting", "Monetary Policy", "Exchange Rate Policy", "Fiscal Policy", "Supply Side Policy", "Economic Growth", "Unemployment"]
                }
        topic_toFind = topics[subject]
        topic_choice = process.extract(user_input, topic_toFind, limit=1)
        print(topic_choice[0][0])
        return topic_choice