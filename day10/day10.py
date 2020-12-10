#!/usr/bin/python3

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data


def part1(data = False):
    if not data:
        data = read_input('input')
    data0 = [int(d) for d in data]
    data0.sort()
    data1 = data0.copy()
    data1.insert(0,0)
    data0.append(data0[-1]+3)
    delta = [a-b for a,b in zip(data0,data1)]
    return delta.count(1) * delta.count(3)

def count_charger_arrangements(data):
    if len(data) == 1:
        return 1
    i = 1
    sum_arrangements = 0
    while i < len(data) and data[i] - data[0] <= 3:
        sum_arrangements += count_charger_arrangements(data[i:])
        i = i+1
    return sum_arrangements

def part2_rec(data = False):
    if not data:
        data = read_input('input')
    data = [int(d) for d in data]
    data.sort()
    data.insert(0,0)
    data.append(data[-1]+3)
    return count_charger_arrangements(data)

def part2(data=False):
    if not data:
        data = read_input('input')
    data = [int(d) for d in data]
    data.sort()
    jmp_dict = {0: 1}
    for j,value in enumerate(data):
        jmp_dict[value] = 0
        for i in range(1,4):
            if value - i in jmp_dict:
                jmp_dict[value] += jmp_dict[value-i]
    return jmp_dict[data[-1]]


def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 35
    print("Test 1 OK")
    data = read_input('test_input_2')
    assert part1(data) == 220
    print("Test 2 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert part2(data) == 8
    print("Test 1 OK")
    data = read_input('test_input_2')
    assert part2(data) == 19208
    print("Test 2 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
