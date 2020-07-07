import asyncio
from typing import List, Dict
from pyramid.view import view_config
from . import controller


@view_config(route_name='book_search', request_method='POST', renderer='json')
def search_books(request) -> List[List[Dict[str, str]]]:
    """Search Books View

    Route Name
    ----------
    `book_search`

    Request Mode
    ------------
    POST

    Parameters
    ----------
    These parameters should be passed in JSON Request Body.

    limit: int
       Maximum number of results per query.
       Limit cannot be less than 1 or greater than 50.
    queries: list
       Query strings passed in a list.

    Response Code
    -------------
    200 OK
    400 BAD REQUEST
    500 INTERNAL SERVER ERROR

    Response
    --------
    A JSON response is sent back for response code `200 OK`.

    :return: List of List of Search Results for Multiple Queries.
    :rtype: List[List[Dict[str, str]]]
    """
    try:
        database = request.registry.settings['database']
    except KeyError:
        request.response.status = 500
        return {
            "error": "Internal Server Error",
            "description": "Database not setup in config."
        }

    try:
        limit = request.json_body['limit']
        queries = request.json_body['queries']
    except KeyError as e:
        request.response.status = 400
        return {
            "error": "Bad Request",
            "description": f"Mandatory json body parameter {e} is missing."
        }

    if not isinstance(limit, int):
        request.response.status = 400
        return {
            "error": "Bad Request",
            "description": "Limit must be an integer."
        }
    else:
        if limit < 1 or limit > 50:
            request.response.status = 400
            return {
                "error": "Bad Request",
                "description": "Limit can't be less than 1 or greater than 50."
            }

    multi_search_results = list()
    documents = set()
    for query in queries:
        try:
            res = controller.search_book_index(query, limit, database)
        except LookupError:
            res = None
        if res:
            documents |= set([book['id'] for book in res])
            multi_search_results.append(res)
        else:
            multi_search_results.append([])

    authors = asyncio.run(controller.get_authors(documents))
    for results in multi_search_results:
        if results:
            for doc in results:
                doc['author'] = authors[doc['id']]
    request.response.status_code = 200
    return multi_search_results
