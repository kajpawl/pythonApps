import requests
import bs4


def main():
    print_header()

    country_code = input('What country do you want the weather for? (PL) ').lower()
    city = input('What city do you want the weather for? (Katowice) ').lower()

    html = get_html_from_web(country_code, city)

    get_weather_from_html(html)
    # get html from web
    # parse the html
    # display the forecast


def print_header():
    print('-------------------------------------------')
    print('                WEATHER APP')
    print('-------------------------------------------')
    print()


def get_html_from_web(country_code, city):
    url = 'https://www.wunderground.com/weather/{}/{}'.format(country_code, city)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup)


if __name__ == '__main__':
    main()
