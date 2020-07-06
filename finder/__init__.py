from pyramid.config import Configurator


def main(global_config, **settings):
    """ Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:

        # Project : Books Finder
        config.include('.routes')
        config.scan('finder')

    return config.make_wsgi_app()
