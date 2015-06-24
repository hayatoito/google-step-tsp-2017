#!/usr/bin/env python3

import random

CHALLENGE_SIZES = (5, 8, 16, 64, 128, 512, 2048)


def generate_cities(n, max_x=1600.0, max_y=900.0, seed=1):
    random.seed(seed)
    for i in range(n):
        yield random.uniform(0, max_x), random.uniform(0, max_y)


def main():
    for i, n in enumerate(CHALLENGE_SIZES):
        with open('input_{}.csv'.format(i), 'w') as f:
            f.write('x,y\n')
            for x, y in generate_cities(n):
                f.write('{},{}\n'.format(x, y))


if __name__ == '__main__':
    main()
