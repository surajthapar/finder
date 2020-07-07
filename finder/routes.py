"""API urls

:Route Name: book_search
:Route URL: /search/

"""


def includeme(config):
    config.add_route('book_search', '/search/')
