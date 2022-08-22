from cgitb import text
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

# job_elements = results.find_all('div', class_='card-content')

# for job_element in job_elements:
# title_element = job_element.find('h2', class_='title')
# company_element = job_element.find('h3', class_='company')
# location = job_element.find('p', class_='location')
# print(title_element.text.strip())
# print(company_element.text.strip())
# print(location.text.strip())
# print()

# python_jobs = results.find_all(
#     'h2', string=lambda text: 'python' in text.lower())

# for python_job in python_jobs:
# parent_element = python_job.parent.parent.parent
# title_element = parent_element.find('h2', class_='title')
# company_element = parent_element.find('h3', class_='company')
# location = parent_element.find('p', class_='location')
# apply_link = parent_element.find_all('a')[1]
# print(title_element.text.strip())
# print(company_element.text.strip())
# print(location.text.strip())
# print(apply_link['href'].strip())
# print()


def find_jobs_by_title(query):
    jobs = results.find_all('h2', string=lambda text: query in text.lower())
    for job in jobs:
        parent_element = job.parent.parent.parent
        title_element = parent_element.find('h2', class_='title')
        company_element = parent_element.find('h3', class_='company')
        location = parent_element.find('p', class_='location')
        apply_link = parent_element.find_all('a')[1]
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location.text.strip())
        print(apply_link['href'].strip())
        print()


find_jobs_by_title(query='python')
