# ------------------------------------------------------------------------------------------------ #
#                                 Web Scrapping with BeautifulSoup                                 #
# ------------------------------------------------------------------------------------------------ #

from bs4 import BeautifulSoup

with open("day_45/website.html") as html_file:
    contents = html_file.read()


soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())

# ---------------------------- Accessing Tags and Strings within Tags ---------------------------- #
print(soup.title)  # Prints the title tag: <title>Angela's Personal Site</title>
print(soup.title.name)  # Prints the string inside the title: Angela's Personal Site
print(soup.a)  # Prints the first anchor tag in the HTML file

# -------------------------------------- Accessing ALL Tags -------------------------------------- #
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))


# ------------------------------------- Accessing by Tag & ID ------------------------------------ #
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.get("class"))

# -------------------------------------- Drilling Using CSS -------------------------------------- #

# Selecting the first instance of an anchor tag inside a paragraph tag
company_url = soup.select_one(selector="p a")
print(company_url)

# Selecting the first instance where an ID is 'name'
name = soup.select_one(selector="#name")
print(name)

# Selecting all isntances where the class name is 'heading'
heading_all = soup.select(".heading")
print(heading_all)

# ----------------------------------- Scrapping a Live Website ----------------------------------- #

import requests
import pprint

# Getting back an HTML document using requests API call
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup2 = BeautifulSoup(yc_web_page, "html.parser")
print(soup2.title)


# Creating lists to hold results
article_texts = []
article_links = []


articles = soup2.find_all(name="span", class_="titleline")

# Grabbing the article names and links
for article_tag in articles:
    article_texts.append(article_tag.find("a").getText())
    article_links.append(article_tag.find("a").get("href"))

# Grabbing the article votes
article_votes = [
    int(score.getText().split()[0])
    for score in soup2.find_all(name="span", class_="score")
]

# Printing the lists
pprint.pprint(article_texts)
pprint.pprint(article_links)
pprint.pprint(article_votes)

# Finding index of highest upvoted article
largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)

# Finding the article text and article link for the highest upvoted article
print(article_texts[largest_index + 1])
print(article_links[largest_index + 1])
