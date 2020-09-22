import movie_svc


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
        except:
            print('YIKES, that didn\'t work!')

    print('Exiting...')


if __name__ == '__main__':
    main()
