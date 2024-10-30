from bs4 import BeautifulSoup
import requests


# with open ("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# name = company_url = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("span", attrs={"class": "titleline"})
article_texts = [article_tag.getText() for article_tag in articles]
article_links = [article_link.find("a").get("href") for article_link in articles]
articles_votes = soup.find_all("span", attrs={"class": "score"})
article_upvotes = [int(article_upvote.getText().split()[0]) for article_upvote in articles_votes]

largest = max(article_upvotes)
largest = article_upvotes.index(largest)

print(article_texts[largest])
print(article_links[largest])