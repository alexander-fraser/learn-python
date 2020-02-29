# Decode Webpage
# Alexander Fraser
# 28 February 2020

"""
Requirements:
- requests
- bs4

Use the BeautifulSoup and requests Python packages to
print out a list of all the article titles on the
New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup


def pull_website(url):
    # Collect and parse the webpage's HTML.
    webpage_get = requests.get(url)
    webpage = webpage_get.text
    soup = BeautifulSoup(webpage, 'html.parser')
    
    # Pulls all the headings (h2) from the webpage.
    for heading in soup.find_all(class_='css-1ee8y2t'):
        print(heading.h2.text.replace('\n', ' ').strip())          


def main():
    url = 'https://www.nytimes.com/'
    pull_website(url)


if __name__ == "__main__":
    main()