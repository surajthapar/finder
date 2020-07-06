"""Books Indexing Script

This script uses Scout to index book summary data. This index is
later used for realtime searches.

Make sure you include this script's relative import path in
setup.py; Specifically, setup –> entry_points –> console_scripts.
You may launch the script by calling it from the virtualenv using
pipenv. You must include the configuration file, e.g. env.ini

To install the script,

    $ pipenv install -e "."

To run the script,

    $ pipenv run index env.ini --corpus data.json

OR

    $ pipenv run index env.ini --corpus data.json --database custom.db --slicing [2,5,7]

"""

from pyramid.paster import setup_logging
from scout import Index
import argparse
import sys
import json
import logging
log = logging.getLogger(__name__)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., env.ini',
    )
    parser.add_argument('--corpus',
                        help='Location of the books json dump.',
                        required=True)
    parser.add_argument('--database',
                        help='SQLite3 db-name, to store corpus.',
                        default='scout.db',
                        required=False)
    parser.add_argument('--slicing',
                        help='Index slicing param for partitioning.',
                        default='[1, 2]',
                        required=False)
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    log.info("Environment setup in progress.")
    args = parse_args(argv)
    setup_logging(args.config_uri)
    slices = json.loads(args.slicing)

    log.info("Calling scout.Index, please hold on.")
    idx = Index(args.corpus, args.database, slices)
    log.info("Registering index, this may take some time.")
    idx.register()
    log.info(f"Index registration completed. (sqlite :{args.database})")
