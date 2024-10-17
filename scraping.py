import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://news.google.com/search?q=malaria+outbreaks'

response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the page!")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

# Extract article titles and links
articles = soup.find_all('article')

outbreak_articles = []

# Iterate over the articles and extract the relevant information
for article in articles:
    headline = article.find('a', class_ = "JtKRv").text  # Extract the headline
    link = article.find('a', class_ = "JtKRv")['href']   # Extract the link
    full_link = "https://news.google.com" + link[1:]    # Construct full link
    date = article.find('time', class_ = "hvbAAd")['datetime'][0:10]

    # Search for outbreak-related keywords in the headline or summary
    keywords = ['outbreak', 'epidemic', 'rise', 'increase', 'double', 'triple']
    if any(keyword.lower() in (headline ).lower() for keyword in keywords):
        outbreak_articles.append({
            'headline': headline,
            'link': full_link,
            'date': date
        })

print(f"Scraped {len(outbreak_articles)} articles related to outbreaks.")

article_df = pd.DataFrame(outbreak_articles)
article_df.to_csv("articles.csv", index=False)

print(article_df)