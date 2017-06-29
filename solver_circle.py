#!/usr/bin/env python3
# coding: UTF-8

import sys
import math

from common import print_solution, read_input


class Rectangle:
	def __init__(self, x_m, x_M, y_m, y_M):
		self.x_min = x_m
		self.x_MAX = x_M
		self.y_min = y_m
		self.y_MAX = y_M
	

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


x_mid = 0
y_mid = 0
def distanceFromMidTo(city):
	return math.sqrt((x_mid - city[0]) ** 2 + (y_mid - city[1]) ** 2)

def solve(cities):
    N = len(cities)
    coordinates_x = []
    coordinates_y = []

    # 都市間の距離を計算
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    
    for i in range(N):
    	coordinates_x.append(cities[i][0])
    	coordinates_y.append(cities[i][1])

    x_min = min(coordinates_x)
    x_MAX = max(coordinates_x)
    y_min = min(coordinates_y)
    y_MAX = max(coordinates_y)

    # 境界線上の都市のために最大値を+1する
    rectangle_MAX = Rectangle(x_min, x_MAX + 1, y_min, y_MAX + 1)

    # 範囲の中心
    x_mid = (x_MAX - x_min) / 2
    y_mid = (y_MAX - y_min) / 2

    fraction_size = 4
    fraction_unit_x = (x_MAX - x_min)/fraction_size * 2
    fraction_unit_y = (y_MAX - y_min)/fraction_size * 2

    # 中心から徐々に広げていく範囲の配列を生成
    range_rectangles = [rectangle_MAX]
    for i in range(1, fraction_size - 1):
    	x_m = fraction_unit_x * i
    	x_M = fraction_unit_x * (fraction_size * 2 - i)
    	y_m = fraction_unit_y * i
    	y_M = fraction_unit_y * (fraction_size * 2- i)
    	r = Rectangle(x_m, x_M, y_m, y_M)
    	range_rectangles.insert(0, r)


    search_cities = []
    current_city = -1
    unvisited_cities = set(range(0, N))

    solution = []

    def distance_from_current_city(to):
        return dist[current_city][to]


    for r in range_rectangles:
    		
    		for j in unvisited_cities:
    			if r.x_min <= coordinates_x[j] and coordinates_x[j] < r.x_MAX and r.y_min <= coordinates_y[j] and coordinates_y[j] < r.y_MAX:
    				search_cities.append(j)

    		# 初めの探索の場合、最も中点に近い都市を見つける
    		if current_city == -1:
    			dist_from_mid = x_MAX ** 2
    			for j in search_cities:
    				d = distanceFromMidTo(cities[j])
    				if d < dist_from_mid:
    					dist_from_mid = d
    					current_city = j

    			if current_city != -1:
    				unvisited_cities.remove(current_city)
    				search_cities.remove(current_city)
    				solution.append(current_city)

    		while search_cities:
    			next_city = min(search_cities, key=distance_from_current_city)
    			unvisited_cities.remove(next_city)
    			search_cities.remove(next_city)
	    		solution.append(next_city)
	    		current_city = next_city

    return solution

# def save(solution):
# 	challenge = 0
# 	if len(solution) == 8:
# 		challenge = 1
# 	elif len(solution) == 16:
# 		challenge = 2
# 	elif len(solution) == 64:
# 		challenge = 3
# 	elif len(solution) == 128:
# 		challenge = 4
# 	elif len(solution) == 512:
# 		challenge = 5
# 	elif len(solution) == 2048:
# 		challenge = 6

# 	with open('solution_circle_{}.csv'.format(challenge)) as f:
# 		f.write('index\n')
# 		for i in solution:
# 			f.write('{}\n'.format(solution))
# 	print('success to save')

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
    # save(solution)
