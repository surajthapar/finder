from pyramid.view import view_config


@view_config(route_name='book_search', request_method='POST', renderer='json')
def search_books(request):
    request.response.status_code = 200
    return {"status": "OK"}
