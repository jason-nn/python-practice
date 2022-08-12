from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"


def get_soup_from_url(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup


soup = get_soup_from_url(url=url)

text = soup.get_text()
print(text)

images = soup.find_all('img')
print(images)

sources = [image['src'] for image in images]
print(sources)


print(soup.title)
print(soup.title.string)

print(soup.find_all("img", src="/static/dionysus.jpg"))
