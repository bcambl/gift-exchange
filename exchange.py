#!/usr/bin/env python
"""
Gift-Exchange
=============
Randomly generate a gift exchange for a list of people and ensures
noone in the list receives their own name nor their significant other.
Also ensure people do not gift the same person on consecutive exchanges.
"""
__author__ = 'Blayne Campbell'
__date__ = '2014/10/12'

import datetime
import random
import json
import os

# all people in the gift exchange
people = ['Person1', 'Person2', 'Person3', 'Person4',
          'Person5', 'Person6', 'Person7']

# restrictions (couples should not buy for each other)
couple = [['Person1', 'Person2'],
          ['Person3', 'Person4'],
          ['Person5', 'Person6']]

history_file = "history.json"

class Person(object):
    def __init__(self, name=None):
        self.name = name
        self.give = None
        self.receive = None
        self.couple = []


gx = dict((name, Person(name=name)) for name in people)


def get_history():
    if os.path.isfile(history_file):
        with open(history_file, "r") as f:
            history = json.load(f)
        return history
    history = {}
    for p in people:
        history[p] = ""
    return history


def set_history():
    history = {}
    for p in people:
        history[gx[p].name] = gx[p].give
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)


def generate_exchange(history):
    random.shuffle(people)
    itertimes = 0
    max_itertimes = (len(people) * 10)
    for p in people:
        while itertimes < max_itertimes:
            pick = random.choice(people)
            if not gx[p].couple:
                for c in couple:
                    if pick in c and p in c:
                        gx[p].couple = c
            if gx[p].name != pick and \
                    not gx[pick].receive and \
                    pick not in gx[p].couple and \
                    not gx[pick].give == p and \
                    not history[p] == pick:
                gx[p].give = pick
                gx[pick].receive = p
                break
            else:
                itertimes += 1
                continue


def reset_exchange():
    for p in people:
        gx[p].give = None
        gx[p].receive = None


def invalid_exchange():
    invalid = False
    for p in people:
        if gx[p].receive:
            pass
        else:
            invalid = True
    return invalid


def display_exchange():
    print("\nGift Exchange Members:")
    for p in people:
        print(p)
    print("\nExchange Restrictions:")
    for p1, p2, in couple:
        print("%s <-> %s" % (p1, p2))

    print("\n===================================\n"
          "Gift Exchange\n"
          "Generated on: %s\n"
          "==================================="
          % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    for p in people:
        print("%s: Gives to: %s and receives from: %s"
              % (gx[p].name, gx[p].give, gx[p].receive))
    print("\n")


def main():
    # load previous exchange history
    history = get_history()
    # randomly generate the gift exchange until it passes all validations
    while invalid_exchange():
        reset_exchange()
        generate_exchange(history)
    # display the gift exchange results
    display_exchange()
    # write history if exchange validates
    if not invalid_exchange():
        set_history()


if __name__ == "__main__":
    main()
