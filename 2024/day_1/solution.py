import numpy as np


def read_input_lists(filename):
    lists = np.loadtxt(filename, dtype=int)
    list_1, list_2 = lists[:,0], lists[:,1]
    list_1= sorted(list_1.tolist())
    list_2 = sorted(list_2.tolist())
    return list_1, list_2

def solve_part1():
    list_1, list_2 = read_input_lists('input.txt')
    result= sum(abs(np.subtract(list_1,list_2)))
    print('Part 1 result: ', result)

def solve_part2():
    list_1, list_2 = read_input_lists('input.txt')
    similarities = [num*list_2.count(num) for num in list_1]
    print('Part 2 result: ', sum(similarities))

def main():
    solve_part1()
    solve_part2()

if __name__ == "__main__":
    main()