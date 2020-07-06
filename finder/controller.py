import aiohttp
import asyncio
from scout import Scout
from .exceptions import UnresponsiveAuthorAPI


def search_book_index(query, limit, database):
    sc = Scout(database)
    return [{
        "id": r['id'],
        "summary": r['summary'],
        "query": query
    } for r in sc.search(query, limit)]


async def get_authors(ids):

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

    return await asyncio.gather(*[hit_author(id) for id in ids])
