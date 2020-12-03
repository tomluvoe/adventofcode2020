#!/usr/bin/python3

import re

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1].split('\n')

def _read_policy(data):
    r0, r1, char, pwd = re.search(r'(\d+)\-(\d+) (\w): (\w+)', data).groups()
    return pwd, char, [int(r0), int(r1)]

def part1(data):
    count = 0
    for dat in data:
        pwd, char, range = _read_policy(dat)
        if pwd.count(char) >= range[0] and pwd.count(char) <= range[1]:
            count += 1
    return count

def part2(data):
    count = 0
    for dat in data:
        pwd, char, range = _read_policy(dat)
        if (pwd[range[0]-1] == char or pwd[range[1]-1] == char) and \
            not pwd[range[0]-1] == pwd[range[1]-1]:
            count += 1
    return count

def unit_test_p1():
    print("Unit test start:")
    assert part1(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2
    print("Test 1 OK")

def unit_test_p2():
    print("Unit test start:")
    assert part2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 1
    print("Test 1 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(data), "\n")
