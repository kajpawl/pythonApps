import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score')


def main():
    print_header()
    search_text = get_search_text()
    get_movies(search_text)


def print_header():
    print('---------------------------------------')
    print('           MOVIE SEARCH APP')
    print('---------------------------------------')
    print()


def get_search_text():
    return input('Enter search phrase (movie title): ').lower()


def get_movies(search_text):
    url = 'http://movieservice.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    # movies = []
    # for md in movies_list:
    #     m = MovieResult(
    #         imdb_code=md.get('imdb_code'),
    #         title=md.get('title'),
    #         director=md.get('director'),
    #         keywords=md.get('keywords'),
    #         duration=md.get('duration'),
    #         genres=md.get('genres'),
    #         rating=md.get('rating', 0),
    #         year=md.get('year', 0),
    #         imdb_score=md.get('imdb_score', 0.0)
    #     )
    #     movies.append(m)

    # movies = []
    # for md in movies_list:
    #     m = MovieResult(**md)
    #     movies.append(m)

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    print('Found {} movies for search {}.'.format(len(movies), search_text))
    for m in movies:
        print("{} -- {}".format(m.year, m.title))


if __name__ == '__main__':
    main()
