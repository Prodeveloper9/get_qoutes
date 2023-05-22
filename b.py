import requests
import bs4
import random

qoute_type = input("What type of qoute you want: -love  -Science    -life   -philosophy         ")
q = qoute_type
html = requests.get("https://www.goodreads.com/quotes/tag/" + q).text
html_parser = bs4.BeautifulSoup(html, "lxml")
all_quotes = html_parser.findAll("div", attrs={"class": "quoteText"})
random_number = random.randint(1, 30)
