#!/usr/bin/env python3

import math

from common import read_input

CHALLENGES = 7


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def verify_solutions():
    solutions = ('random', 'greedy', 'sa', 'yours')
    for challenge_number in range(CHALLENGES):
        print('Challenge {}'.format(challenge_number))
        cities = read_input('input_{}.csv'.format(challenge_number))
        N = len(cities)
        for solution_name in solutions:
            solution_file = 'solution_{}_{}.csv'.format(solution_name,
                                                        challenge_number)
            with open(solution_file) as f:
                lines = f.readlines()
                assert lines[0].strip() == 'index'
                tour = [int(i.strip()) for i in lines[1:N + 1]]
            assert set(tour) == set(range(N))
            path_length = sum(distance(cities[u], cities[v])
                              for u, v in zip(tour, tour[1:] + tour[0:1]))
            print('{:8}: {:>10.2f}'.format(solution_name, path_length))
        print()


if __name__ == '__main__':
    verify_solutions()
