def main():
    print_header()

    country_code = input('What country do you want the weather for? (PL) ').lower()
    city = input('What city do you want the weather for? (Katowice) ').lower()

    get_html_from_web(country_code, city)

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
    print(url)
    requests


if __name__ == '__main__':
    main()
