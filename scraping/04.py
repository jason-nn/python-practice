import mechanicalsoup
from time import sleep

browser = mechanicalsoup.Browser()


def get_result():
    url = "http://olympus.realpython.org/dice"
    page = browser.get(url)
    tag = page.soup.select("#result")[0]
    result = tag.text

    print(f"The result of your dice roll is: {result}")

    sleep(3)
    get_result()


get_result()
