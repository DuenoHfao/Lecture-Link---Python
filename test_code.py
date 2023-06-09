import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=9mgTJR_FpyU"    
reqs = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# displaying the title
for title in soup.find_all('title'):
    print(title.get_text())
