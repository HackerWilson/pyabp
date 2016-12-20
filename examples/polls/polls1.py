#!/usr/bin/env python
# encoding: utf-8

"""Group Polls 1
# Polls

Polls is a simple API allowing consumers to view polls and vote in them. You can view this documentation over at [Apiary](http://docs.pollsapi.apiary.io).
"""


def a():
    """
    # Polls API Root [/]

    This resource does not have any attributes. Instead it offers the initial API affordances in the form of the links in the JSON body.

    It is recommend to follow the "url" link values, [Link](https://tools.ietf.org/html/rfc5988) or Location headers where applicable to retrieve resources. Instead of constructing your own URLs, to keep your client decoupled from implementation details.

    ## Retrieve the Entry Point [GET]

    + Response 200 (application/json)

        {
            "questions_url": "/questions"
        }
    """


def b():
    """Group Question 1
    ## Question [/questions/{question_id}]

    A Question object has the following attributes:

    + question
    + published_at - An ISO8601 date when the question was published.
    + url
    + choices - An array of Choice objects.

    + Parameters
        + question_id: 1 (required, number) - ID of the Question in form of an integer

    ### View a Questions Detail [GET]

    + Response 200 (application/json)

        {
            "question": "Favourite programming language?",
            "published_at": "2014-11-11T08:40:51.620Z",
            "url": "/questions/1",
            "choices": [
                {
                    "choice": "Swift",
                    "url": "/questions/1/choices/1",
                    "votes": 2048
                }, {
                    "choice": "Python",
                    "url": "/questions/1/choices/2",
                    "votes": 1024
                }, {
                    "choice": "Objective-C",
                    "url": "/questions/1/choices/3",
                    "votes": 512
                }, {
                    "choice": "Ruby",
                    "url": "/questions/1/choices/4",
                    "votes": 256
                }
            ]
        }
    """


class c():
    """Group Question 2
    ## Questions Collection [/questions{?page}]

    + Parameters
        + page: 1 (optional, number) - The page of questions to return

    ### List All Questions [GET]

    + Response 200 (application/json)

        + Headers

                Link: </questions?page=2>; rel="next"

        + Body

                [
                    {
                        "question": "Favourite programming language?",
                        "published_at": "2014-11-11T08:40:51.620Z",
                        "url": "/questions/1",
                        "choices": [
                            {
                                "choice": "Swift",
                                "url": "/questions/1/choices/1",
                                "votes": 2048
                            }, {
                                "choice": "Python",
                                "url": "/questions/1/choices/2",
                                "votes": 1024
                            }, {
                                "choice": "Objective-C",
                                "url": "/questions/1/choices/3",
                                "votes": 512
                            }, {
                                "choice": "Ruby",
                                "url": "/questions/1/choices/4",
                                "votes": 256
                            }
                        ]
                    }
                ]
    """
