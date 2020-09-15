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
    location = soup.find(class_='city-header').find('h1').find('span').get_text()
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temperature = soup.find(class_='wu-unit-temperature').get_text()

    location = find_city_and_text_from_location(cleanup_text(location)) + ':'
    condition = cleanup_text(condition) + ','
    temperature = cleanup_text(temperature)

    print(location, condition, temperature)


def find_city_and_text_from_location(text: str):
    parts = text.split(' Weather Conditions')
    return parts[0]


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
