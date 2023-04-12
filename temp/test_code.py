import requests
from bs4 import BeautifulSoup


topics = {
        "Physics": [],
        "Chemistry": ["Atomic Structure", "Atoms, Molecules and Stoichiometry & Redox", "Chemical Bonding", "The Gaseous State", "Chemical Energetics I", "Chemical Energetics II", "Reaction Kinetics", "Chemical Equilibria", "Solubility Equilibria", "Introduction to Organic Chemistry", "Alkanes", "Alkenes", "Arenes", "The Periodic Table", "Theories of Acids and Bases", "Halogen Derivatives", "Hydroxy Compounds", "Carbonyl Compounds", "Carboxylic Acids and Derivatives", "Nitrogen Compounds", "Electrochemistry", "Electrolytic Cell", "Transition Element", "Galvanic Cell"],
        "Mathematics": [],
        "Economics": ["Central Economic Problem", "Basics of Market Economy", "Market Economy", "Elasticity Concepts", "Market Failure", "Equity", "Firms and Decisions", "Cost of Production", "Market Structure", "Decisions and Strategies of Firms", "Introduction to Macroeconomics", "National Income Accounting", "Monetary Policy", "Exchange Rate Policy", "Fiscal Policy", "Supply Side Policy", "Economic Growth", "Unemployment"]
        }

url = "https://www.youtube.com/watch?v=9mgTJR_FpyU"    
reqs = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# displaying the title
for title in soup.find_all('title'):
    print(title.get_text())
