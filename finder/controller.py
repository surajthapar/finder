import aiohttp
import asyncio
from typing import List, Dict
from scout import Scout
from .exceptions import UnresponsiveAuthorAPI


def search_book_index(query: str,
                      limit: int,
                      database: str
                      ) -> List[Dict[str, str]]:
    """Search book index uses Scout search engine to fetch results.

    :param query: User input query terms.
    :type query: str
    :param limit: Maximum results to fetch.
    :type limit: int
    :param database: Scout index SQLite3 database file.
    :type database: str
    :return: List of results with Book's id, summary and query.
    :rtype: List[Dict[str, str]]

    """
    sc = Scout(database)
    return [{
        "id": r['id'],
        "summary": r['summary'],
        "query": query
    } for r in sc.search(query, limit)]


async def get_authors(ids: List[str]) -> Dict[str, str]:
    """Get authors asynchronously fetches Book Authors from Author API.

    Author API is hit in async manner. This reduces the load time by
    5 folds in 10 results.

    TODO : Caching implementation to reduce server load.

    :param ids: List of book id.
    :type ids: List[str]
    :return: Dictionary map of (id, author).
    :rtype: Dict[str, str]

    """
    async def hit_author(id):
        endpoint = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"

        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint,
                                    json={"book_id": id},
                                    ssl=False
                                    ) as response:
                if response.status == 200:
                    js = await response.json()
                    return (id, js['author'])
                else:
                    raise UnresponsiveAuthorAPI(
                                f"Response Code : {response.status}"
                            )
    # Return a dictionary of all requested authors
    # {"34": "Judith Rich Harris", "3": "James Webb Young"}
    return {
                id: author
                for id, author in await asyncio.gather(
                    *(hit_author(id) for id in ids)
                )
            }
