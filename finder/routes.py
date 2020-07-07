"""List of API urls

| Route Name  | URL      |
--------------------------
| book_search | /search/ |

"""


def includeme(config):
    config.add_route('book_search', '/search/')
