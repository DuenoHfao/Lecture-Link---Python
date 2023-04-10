import requests
from bs4 import BeautifulSoup

def get_title(url):
# making requests instance
    reqs = requests.get(url)
    
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    # displaying the title
    for title in soup.find_all('title'):
        print(title.get_text())
    
    return title.get_text()