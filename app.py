import bs4 as bs4
import requests as requests

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_method():
    return 'Yay! This is working!'


@app.route("/q/<question>")
def greet(question):
    postRequest = requests.get("https://www.google.com/search?q=" + question)
    result = findByClass(postRequest.text, "BNeawe s3v9rd AP7Wnd")
    return result


def findByClass(text, className):
    soup = bs4.BeautifulSoup(text, 'lxml')
    result = soup.find_all("div", {"class": className})

    try:
        return result[0].getText()
    except:
        return "no result found"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
