#!/usr/bin/python3

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1].split('\n')
    return data

def calculate_slope(data, right_steps=3, down_steps=1):
    if not data:
        data = read_input('input')
    right = 0
    trees = 0
    line = down_steps
    while line < len(data):
        right = (right + right_steps) % len(data[line])
        trees = trees + 1 if data[line][right] == '#' else trees
        line += down_steps
    return trees

def part1(data = False):
    if not data:
        data = read_input('input')
    return calculate_slope(data, 3, 1)

def part2(data = False):
    if not data:
        data = read_input('input')
    ret = calculate_slope(data, 1, 1)
    ret *= calculate_slope(data, 3, 1)
    ret *= calculate_slope(data, 5, 1)
    ret *= calculate_slope(data, 7, 1)
    ret *= calculate_slope(data, 1, 2)
    return ret

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 7
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert calculate_slope(data, 1, 1) == 2
    print("Test 1 OK")
    assert calculate_slope(data, 3, 1) == 7
    print("Test 2 OK")
    assert calculate_slope(data, 5, 1) == 3
    print("Test 3 OK")
    assert calculate_slope(data, 7, 1) == 4
    print("Test 4 OK")
    assert calculate_slope(data, 1, 2) == 2
    print("Test 5 OK")
    assert part2(data) == 336
    print("Test 6 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
