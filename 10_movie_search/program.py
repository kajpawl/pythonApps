import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------------------------------')
    print('           MOVIE SEARCH APP')
    print('---------------------------------------')
    print()


def search_event_loop():
    search_text = 'ONCE_THROUGH_LOOP'

    while search_text != 'x':
        try:
            search_text = input('Movie search text (x to exit): ').lower()
            if search_text != 'x':
                results = movie_svc.find_movies(search_text)
                print('Found {} movies for search {}.'.format(len(results), search_text))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
                print()
        except ValueError as ve:
            print(ve)
        except requests.exceptions.ConnectionError:
            print('Error: Your network is down. Please check your connection.')
        except requests.exceptions.HTTPError:
            print('Error: Content not found. Enter valid search phrase.')
        except Exception as x:
            print('Unexpected error. Details: {}. Error type: {}'.format(type(x), x))

    print('Exiting...')


if __name__ == '__main__':
    main()
