def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_solution(solution):
    first_line = 'index'
    solution_as_strings = [str(v) for v in solution]
    other_lines = '\n'.join(solution_as_strings)
    return first_line + '\n' + other_lines


def print_solution(solution):
    print(format_solution(solution))
