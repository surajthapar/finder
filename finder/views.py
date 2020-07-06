from pyramid.view import view_config
from . import controller


@view_config(route_name='book_search', request_method='POST', renderer='json')
def search_books(request):
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

    results = list()
    for query in queries:
        results.append(controller.search_book_index(query, limit, database))

    request.response.status_code = 200
    return {"k": limit, "queries": queries, "results": results}
