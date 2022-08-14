from tokenize import group
import mechanicalsoup

browser = mechanicalsoup.Browser()

private_companies_url = 'https://www.ycombinator.com/topcompanies'
public_companies_url = 'https://www.ycombinator.com/topcompanies/public'


def get_main_headquarters(headquarter):
    return headquarter.split(';')[0]


def get_headquarters_list_from_url(url):
    page = browser.get(url)
    headquarters = page.soup.find_all('td', {'class': 'headquarters'})
    return filter(lambda x: len(x) > 0, [get_main_headquarters(headquarter.text) for headquarter in headquarters])


def sort_grouped_headquarters(grouped_headquarters):
    return sorted(grouped_headquarters.items(), key=lambda x: x[1], reverse=True)


def get_grouped_headquarters_from_list(list):
    output = {}
    for headquarter in list:
        if headquarter in output.keys():
            output[headquarter] += 1
        else:
            output[headquarter] = 1
    return sort_grouped_headquarters(output)


def get_headquarters_from_url(url):
    headquarters_list = get_headquarters_list_from_url(url)
    return get_grouped_headquarters_from_list(headquarters_list)


private_companies_headquarters = get_headquarters_from_url(
    private_companies_url)

public_companies_headquarters = get_headquarters_from_url(
    public_companies_url)


print('PRIVATE COMPANIES MAIN HEADQUARTERS')
for headquarters, count in private_companies_headquarters:
    print(f'{headquarters}: {count}')

print()

print('PUBLIC COMPANIES MAIN HEADQUARTERS')
for headquarters, count in public_companies_headquarters:
    print(f'{headquarters}: {count}')
