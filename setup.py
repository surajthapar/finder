#!/usr/bin/env python
from setuptools import setup

setup(
    name='finder',
    version='0.1dev',
    description='Book search API in Python.',
    author='Suraj Thapar',
    author_email='surajthapar.in@gmail.com',
    packages=[
        'finder',
    ],
    install_requires=[
        'scout',
        'plaster_pastedeploy',
        'pyramid',
        'waitress',
        'pyramid_retry',
    ],
    python_requires='>=3.6.5, <4',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Pyramid',
        'Programming Language :: Python :: 3.6.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'paste.app_factory': [
            'main = finder:main',
        ],
    },
)
