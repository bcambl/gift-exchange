#!/usr/bin/env python
"""
Gift-Exchange
=============
Randomly generate a gift exchange for a list of people and ensures
noone in the list receives their own name nor their significant other.
"""
__author__ = 'Blayne Campbell'
__date__ = '2014/10/12'

import datetime
import random

# all people in the gift exchange
people = ['Person1', 'Person2', 'Person3', 'Person4',
          'Person5', 'Person6', 'Person7']

# restrictions (couples should not buy for each other)
couple = [['Person1', 'Person2'],
          ['Person3', 'Person4'],
          ['Person5', 'Person6']]


class Person(object):
    def __init__(self, name=None):
        self.name = name
        self.give = None
        self.receive = None
        self.couple = []


gx = dict((name, Person(name=name)) for name in people)


def generate_exchange():
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
                    not gx[pick].give == p:
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


def verify_exchange():
    nonefound = False
    for p in people:
        if gx[p].receive:
            pass
        else:
            nonefound = True
    return nonefound


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
    # randomly generate the gift exchange until it passes all validations
    while verify_exchange():
        reset_exchange()
        generate_exchange()
    # display the gift exchange results
    display_exchange()


if __name__ == "__main__":
    main()
