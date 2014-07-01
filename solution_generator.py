#!/usr/bin/env python3

import sys
import math

from common import format_solution, read_input

import solver_greedy
import solver_random

CHALLENGES = 7

def generate_sample_solutions():
    solvers = ((solver_random, 'random'),
               (solver_greedy, 'greedy'))
    for challenge_number in range(CHALLENGES):
        cities = read_input('input_{}.csv'.format(challenge_number))
        for solver, solver_name in solvers:
            solution = solver.solve(cities)
            with open('solution_{}_{}.csv'.format(solver_name, challenge_number), 'w') as f:
                f.write(format_solution(solution) + '\n')


if __name__ == '__main__':
    generate_sample_solutions()
