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
