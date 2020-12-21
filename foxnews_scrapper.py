from bs4 import BeautifulSoup   # importing beautiful soup module
import requests     # importing requests module

source = requests.get('https://www.foxnews.com/').text    # getting info from source
soup = BeautifulSoup(source, 'html.parser')   # parsing data from source

for article in soup.find_all("article"):     # running a loop to all articles

    # gathering headline information
    headline = article.h2.text
    print()
    print("Headline: ")
    print(headline)
    print()

    # gathering video information
    video = article.a
    print()
    print("Video: ")
    print(video.get('href'))
    print()
    print("===========================")