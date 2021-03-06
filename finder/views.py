import asyncio
from typing import List, Dict
from pyramid.view import view_config
from . import controller


@view_config(route_name='book_search', request_method='POST', renderer='json')
def search_books(request) -> List[List[Dict[str, str]]]:
    """Search Books View

    :Route Name: `book_search`
    :Request Mode: POST

    These **parameters** should be passed in JSON Request Body.

    limit: int
       Maximum number of results per query.
       Limit cannot be less than 1 or greater than 50.
    queries: list
       Query strings passed in a list.

    **Response**

    :200: OK
    :400: BAD REQUEST
    :500: INTERNAL SERVER ERROR

    A JSON response is sent back for response code `200 OK`.

    .. code-block::

        [
            [
                {
                    "id": 1,
                    "summary": "The Book in Three Sentences: The 10X
                                Rule says that 1) you should set
                                targets for yourself that are 10X
                                greater than what you believe you
                                can achieve and 2) you should take
                                actions that are 10X greater than
                                what you believe are necessary to
                                achieve your goals. The biggest
                                mistake most people make in life is
                                not setting goals high enough. Taking
                                massive action is the only way to
                                fulfill your true potential.",
                    "query": "believe",
                    "author": "Grant Cardone"
                },
                {
                    "id": 28,
                    "summary": "The Book in Three Sentences: This book
                                is a collection of transcriptions from
                                a series of interviews between writer
                                Calvin Tomkins and artist Marcel
                                Duchamp. Duchamp believed strongly in
                                doing work that was free from tradition
                                and starting with as much of a blank
                                slate as possible. He was also quite
                                playful, worked slowly, and saw
                                laziness as a good thing.",
                    "query": "believe",
                    "author": "Calvin Tomkins"
                }
            ],
            [
                {
                    "id": 24,
                    "summary": "The Book in Three Sentences: Over the
                                course of history, human behavior has
                                changed, butnot human nature. No matter
                                who is in power, the rewards gradually
                                accrue to the most clever and talented
                                individuals. Ideas are the strongest
                                things of all in history because they
                                can be passed down and change the
                                behavior of future generations—even a
                                gun was originally an idea.",
                    "query": "changes",
                    "author": "Will and Ariel Durant"
                },
                {
                    "id": 52,
                    "summary": "The Book in Three Sentences: Behavioral
                                problems, not technical skills, are what
                                separate the great from the near great.
                                Incredible results can come from
                                practicing basic behaviors like saying
                                thank you, listening well, thinking
                                before you speak, and apologizing for
                                your mistakes. The first step to change
                                is wanting to change.",
                    "query": "changes",
                    "author": "Marshall Goldsmith"
                }
            ]
        ]


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
