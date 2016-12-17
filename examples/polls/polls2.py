#!/usr/bin/env python
# encoding: utf-8

"""Group Polls 2
# Polls
"""

class d:
    """Group Question 2
    ## Choice [/questions/{question_id}/choices/{choice_id}]

    + Parameters
        + question_id: 1 (required, number) - ID of the Question in form of an integer
        + choice_id: 1 (required, number) - ID of the Choice in form of an integer

    ### Vote on a Choice [POST]

    This action allows you to vote on a question's choice.

    + Response 201

        + Headers

                Location: /questions/1
    """


def e():
    """Group Question 4
    ### Create a New Question [POST]

    You may create your own question using this action. It takes a JSON object containing a question and a collection of answers in the form of choices.

    + question (string) - The question
    + choices (array[string]) - A collection of choices.

    + Request (application/json)

            {
                "question": "Favourite programming language?",
                "choices": [
                    "Swift",
                    "Python",
                    "Objective-C",
                    "Ruby"
                ]
            }

    + Response 201 (application/json)

        + Headers

                Location: /questions/2

        + Body

                {
                    "question": "Favourite programming language?",
                    "published_at": "2014-11-11T08:40:51.620Z",
                    "url": "/questions/2",
                    "choices": [
                        {
                            "choice": "Swift",
                            "url": "/questions/2/choices/1",
                            "votes": 0
                        }, {
                            "choice": "Python",
                            "url": "/questions/2/choices/2",
                            "votes": 0
                        }, {
                            "choice": "Objective-C",
                            "url": "/questions/2/choices/3",
                            "votes": 0
                        }, {
                            "choice": "Ruby",
                            "url": "/questions/2/choices/4",
                            "votes": 0
                        }
                    ]
                }
    """
