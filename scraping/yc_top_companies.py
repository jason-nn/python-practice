import mechanicalsoup

browser = mechanicalsoup.Browser()

private_companies_url = 'https://www.ycombinator.com/topcompanies'
public_companies_url = 'https://www.ycombinator.com/topcompanies/public'


def get_main_headquarters(headquarter):
    return headquarter.split(';')[0]


def get_headquarters_list_from_url(url):
    page = browser.get(url)
    headquarters = page.soup.find_all('td', {'class': 'headquarters'})
    main_headquarters = [get_main_headquarters(
        headquarter.text) for headquarter in headquarters]
    return [main_headquarter for main_headquarter in main_headquarters if len(main_headquarter) > 0]


def get_grouped_headquarters_from_list(list):
    output = {}
    for headquarter in list:
        output[headquarter] = output.get(headquarter, 0)+1
    return output


def sort_grouped_headquarters(grouped_headquarters):
    return sorted(grouped_headquarters.items(), key=lambda x: x[1], reverse=True)


def get_headquarters_from_url(url):
    headquarters_list = get_headquarters_list_from_url(url)
    grouped_headquarters = get_grouped_headquarters_from_list(
        headquarters_list)
    return sort_grouped_headquarters(grouped_headquarters)


private_companies_headquarters = get_headquarters_from_url(
    private_companies_url)

public_companies_headquarters = get_headquarters_from_url(
    public_companies_url)


print('YC TOP PRIVATE COMPANIES MAIN HEADQUARTERS')
for headquarters, count in private_companies_headquarters:
    print(f'{headquarters}: {count}')

print()

print('YC TOP PUBLIC COMPANIES MAIN HEADQUARTERS')
for headquarters, count in public_companies_headquarters:
    print(f'{headquarters}: {count}')
