#!/usr/bin/env python
"""
Gift-Exchange
=============
Randomly generate a gift exchange for a list of people and ensures
noone in the list recieves their own name nor their significant other.
"""
__author__ = 'Blayne Campbell'
__date__ = '2014/10/12'

import datetime
import random

people = ['Bonnie', 'Blayne', 'Christina', 'Keith', 'Michelle', 'John', 'Reg', 'Paul']

couple = [['Blayne', 'Bonnie'],
          ['Keith', 'Christina'],
          ['John', 'Michelle'],
          ['Reg', 'Paul']]


class Person(object):
    def __init__(self, name=None):
        self.name = name
        self.give = None
        self.receive = None
        self.couple = []

gx = dict((name, Person(name=name)) for name in people)


def generate_exchange(max_itertimes):
    random.shuffle(people)
    itertimes = 0
    for p in people:
        while itertimes < max_itertimes:
            pick = random.choice(people)
            if not gx[p].couple:
                for c in couple:
                    if pick in c and p in c:
                        gx[p].couple = c
            if gx[p].name != pick and \
                    not gx[pick].receive and \
                    not pick in gx[p].couple:
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


if __name__ == "__main__":
    max_itertimes = (len(people) * 10)

    while verify_exchange():
        reset_exchange()
        generate_exchange(max_itertimes)

    print("\n============================\n"
          "Gift Exchange\n"
          "Generated on: %s\n"
          "============================"
          % datetime.datetime.now().strftime('%Y-%m-%d'))

    for p in people:
        print("\n%s: Gives to: %s and Recieves from: %s"
              % (gx[p].name, gx[p].give, gx[p].receive))
