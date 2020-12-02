#!/usr/bin/python3

import itertools

input_file = "input"
data = ""

with open(input_file, 'r') as input_file:
    data = input_file.read()[:-1].split('\n')
    data = [int(d) for d in data]

def identify_pair_brute(data, pair_sum):
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            if data[i] + data[j] == pair_sum:
                return [data[i], data[j]]
    return False

def identify_triple_brute(data, triple_sum):
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i == j or j == k or i == k:
                    continue
                if data[i] + data[j] + data[k] == triple_sum:
                    return [data[i], data[j], data[k]]
    return False

def part1(data):
    pair = identify_pair_brute(data, 2020)
    if pair:
        return pair[0] * pair[1]

def part2(data):
    triple = identify_triple_brute(data, 2020)
    if triple:
        return triple[0] * triple[1] * triple[2]

def unit_test_p1():
    print("Unit test start:")
    assert part1([1721, 979, 366, 299, 675, 1456]) == 514579
    print("Test 1 OK")

def unit_test_p2():
    print("Unit test start:")
    assert part2([1721, 979, 366, 299, 675, 1456]) == 241861950
    print("Test 1 OK")

print("My data:\n", data, "\n")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(data), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(data), "\n")
