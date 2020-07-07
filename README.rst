`Finder <https://surajthapar.github.io/finder/index.html>`_ : Book Search API
=====================

**Finder** lets you search the books in bulk via HTTP APIs.

Finder is built on `Pyramid`. It uses `aiohttp` to make async
calls to the API, making it much faster than simple `requests`.
Finder uses `Scout <https://github.com/surajthapar/Scout>`_ to make book search possible.

*Please install* `Scout <https://github.com/surajthapar/Scout>`_ *manually before proceeding.*
-------------------

`GitHub Page : Finder Documentation <https://surajthapar.github.io/finder/index.html>`_

**Book Search APIs**

*Request*

      .. code-block:: bash

         curl --location --request POST 'http://localhost:6543/search/' \
         --header 'Content-Type: application/json' \
         --data-raw '{ "limit" : 10, "queries" : ["believe", "changes"] }'

*Response*
      .. code-block:: javascript

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



`Documentation <https://surajthapar.github.io/finder/index.html>`_
--------------

If you are looking for information on a specific function, class, or method,
this part of the `documentation <https://surajthapar.github.io/finder/index.html>`_ is for you.
