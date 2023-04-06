#!/usr/bin/env python3

"""Monty Hall Simulator

This script runs a simulation of the Monty Hall problem.  By default, it
repeats the problem 10,000 times, and the decision whether to switch is random
with a probability of 0.5.  The number of plays and switching probability can
be altered using the '-n' and '-p' commandline options respectively.

Note that this implementation focuses on readability rather than speed.
"""

import argparse
import random

DEBUG = False
DOOR_CNT = 3

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--play-cnt', type=int, default=10000,
                    help='Number of plays')
parser.add_argument('-p', '--switch-prob', type=float, default=0.5,
                    help='Switch probability')
args = parser.parse_args()
assert 0.0 <= args.switch_prob <= 1.0

if __name__ == '__main__':

    doors = list(range(1, DOOR_CNT + 1))
    wins = 0
    for play in range(args.play_cnt):
        car_door = random.choice(doors)
        if DEBUG:
            print(f'The car is behind door {car_door}.')

        choice = random.choice(doors)
        if DEBUG:
            print(f'The player chooses door {choice}.')

        options = set(doors) - set([car_door, choice])
        open_door = random.choice(list(options))
        if DEBUG:
            print(f'The host opens door {open_door}.')

        switch = random.uniform(0, 1)
        if switch < args.switch_prob:
            options = set(doors) - set([open_door, choice])
            choice = random.choice(list(options))
            if DEBUG:
                print('The player switches door.')
        else:
            if DEBUG:
                print('The player does not switch door.')

        if choice == car_door:
            if DEBUG:
                print('The player won.\n')
            wins += 1
        else:
            if DEBUG:
                print('The player lost.\n')

    print(f'Win probability: {wins / args.play_cnt}')
