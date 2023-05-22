import requests
import bs4
import random
import b

#the inputs
M = input("What is your function :\n1-get qoutes\n\n2-know number qoutes\n3-get a random qoute\n''Please write number''       :")
A = "https://www.goodreads.com/quotes"

#vari
html = requests.get(A).text
html_parser = bs4.BeautifulSoup(html, "html.parser")
quotes = html_parser.findAll("div", attrs={"quoteText"})

#the functions
def get_qoutes():
    for quote in quotes:
        print(quote.text)
def know_numbers_qoutes():
    print(len(html_parser))
def get_a_random_qoute():
    print(b.q)
    while True:
        if b.q == "love" or b.q == "life" or b.q == "science" or b.q == "philosophy":
            html_f = requests.get(A + "/tag/" + b.q).text
        else:
            print("Please try again.")

#dhd
while True:
    if M == "1":
        print(get_qoutes())
        break
    elif M == "2":
        print(know_numbers_qoutes())
        break
    elif M == "3":
        print(get_a_random_qoute())
        html_parser = bs4.BeautifulSoup(html, "lxml")
        all_quotes = html_parser.findAll("div", attrs={"class": "quoteText"})
        random_number = random.randint(1, 30)
        break
    else:
        print("Error\nPlease try again")
        continue