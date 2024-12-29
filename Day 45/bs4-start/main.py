#from bs4 import BeautifulSoup
# import lxml
#
# with open("./website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")   #lxml is a parser
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# #print(soup.prettify())    #idented properly
#
# #print(soup.a)    # gives the first a tag
#
# # print(soup.find_all(name="a"))  #return all the a tags
#
# # all_anchor_tags = (soup.find_all(name="a"))
# #
# # for tag in all_anchor_tags:
# #     #print(tag.getText())
# #     print(tag.get("href"))
#
#
# # heading = soup.find(name="h1", id="name")   #only give match thing
# # # print(heading)
# #
# # section_heading = soup.find(name="h3" , class_="heading")  #we can not only use the 'class' instead 'class_'
# # print(section_heading)
#
#
# #css selector
# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)


#Challenge

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(selector=" .title .titleline a")

article_texts = []
article_links = []
article_scores = []

for article in articles:
    if not article.find("span", class_="sitestr"):
        article_text = article.get_text()
        article_texts.append(article_text)

        link = article.get("href")
        article_links.append(link)

        # Find the parent row and navigate to the score
        parent = article.find_parent("tr")  # Move up to the parent row
        score_element = parent.find_next_sibling("tr").find("span", class_="score")
        if score_element:  # Check if the score exists
            score = score_element.getText().split()[0]  # Extract the number part
            article_scores.append(score)
        else:
            article_scores.append("No score available")


# Print all collected information
# for text, link, score in zip(article_texts, article_links, article_scores):
#     print(f"Title: {text}")
#     print(f"Link: {link}")
#     print(f"Score: {score}")
#     print("-" * 50)


max_num = max(article_scores)
index_max = article_scores.index(max_num)

print(article_texts[index_max] + " and " + article_links[index_max] + " with score " + str(max_num))



















