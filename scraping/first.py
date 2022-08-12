from urllib.request import urlopen
import re

# url = "http://olympus.realpython.org/profiles/aphrodite"
# url = "http://olympus.realpython.org/profiles/poseidon"
url = "http://olympus.realpython.org/profiles/dionysus"


def get_html_from_url(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    return html


def get_title_from_html(html):
    # start_index = html.find('<title>') + len('<title>')
    # end_index = html.find('</title>')
    # title = html[start_index:end_index]
    # return title

    tag_pattern = '<title.*?>.*?</title.*?>'
    match_results = re.search(tag_pattern, html, re.IGNORECASE)
    result_with_tags = match_results.group()
    result = re.sub('<.*?>', '', result_with_tags)
    return result


def get_from_html_with_label(html, label):
    label_start_index = html.find(f'{label}: ')
    value_start_index = label_start_index + len(f'{label}: ')
    value_end_index = value_start_index + html[value_start_index:].find('<')
    raw_value = html[value_start_index:value_end_index]
    return raw_value


html = get_html_from_url(url=url)
print(html)

title = get_title_from_html(html=html)
print(title)

name = get_from_html_with_label(html=html, label='Name')
print(name)

favorite_color = get_from_html_with_label(html=html, label='Favorite Color')
print(favorite_color)
