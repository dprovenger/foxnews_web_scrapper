from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.foxnews.com/').text
soup = BeautifulSoup(source, 'html.parser')

article = soup.find("article")

headline = article.h2.text 
print(headline)
