from scout import Scout


def search_book_index(query, limit, database):
    sc = Scout(database)
    return sc.search(query, limit)
