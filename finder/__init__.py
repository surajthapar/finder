from pyramid.config import Configurator


def main(global_config, **settings):
    """ Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:

        # Project : Books
        config.include('books.routes')
        config.scan('books')

    return config.make_wsgi_app()
