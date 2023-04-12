import requests
from bs4 import BeautifulSoup

def get_title(url):
# making requests instance
    reqs = requests.get(url)
    
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    all_title =  soup.find_all('title')
    print("All Title:", all_title)
    for i in all_title:
        i = str(i).strip()
        print("i:", i)
        findIndex = str(i)[7:len(i)-8]
        print(findIndex)
    
    return all_title