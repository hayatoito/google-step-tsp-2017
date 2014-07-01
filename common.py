def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [tuple(map(float, line.split(','))) for line in lines[1:]]


def format_solution(solution):
    return 'index\n' + '\n'.join(map(str, solution))


def print_solution(solution):
    print(format_solution(solution))
