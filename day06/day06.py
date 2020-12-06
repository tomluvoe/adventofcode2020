#!/usr/bin/python3

import re

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = [d.replace('\n',' ') for d in data.split('\n\n')]
    return data

def anyone_answered_per_group(data):
    answer = ""
    data = data.replace(' ','')
    for c in data:
        answer = answer + c if c not in answer else answer
    return len(answer)

def everyone_answered_per_group(data):
    answer = ""
    data = data.split()
    for i, person in enumerate(data):
        if i > 0:
            new_answer = ""
            for c in person:
                new_answer = new_answer + c if c in answer else new_answer
            answer = new_answer
        else:
            answer = person
    return len(answer)

def part1(data = False):
    if not data:
        data = read_input('input')
    answers = 0
    for group in data:
        answers += anyone_answered_per_group(group)
    return answers

def part2(data = False):
    if not data:
        data = read_input('input')
    answers = 0
    for group in data:
        answers += everyone_answered_per_group(group)
    return answers

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 11
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert everyone_answered_per_group('abc') == 3
    print("Test 1 OK")
    assert everyone_answered_per_group('a\nb\nc') == 0
    print("Test 2 OK")
    assert everyone_answered_per_group('ab\nbc') == 1
    print("Test 3 OK")
    assert everyone_answered_per_group('a\na\na\na\n') == 1
    print("Test 4 OK")
    assert everyone_answered_per_group('b') == 1
    print("Test 5 OK")
    assert part2(data) == 6
    print("Test 6 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
