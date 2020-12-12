#!/usr/bin/python3

import math
import copy

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def rotate_quick(wayp_pos, deg, dir=1):
    for i in range(abs(deg)//90):
        wayp_pos = [-dir*wayp_pos[1], dir*wayp_pos[0]]
    return wayp_pos

def part1(data = False):
    if not data:
        data = read_input('input')
    pos = [0,0]
    dir = 0
    for instr in data:
        param = int(instr[1:])
        if instr[0] in ['L','R']:
            if instr[0] == 'L':
                dir += param
            else:
                dir -= param
            dir = dir % 360
        elif instr[0] in ['N','S','E','W']:
            if instr[0] == 'N':
                pos[1] += param
            elif instr[0] == 'S':
                pos[1] -= param
            elif instr[0] == 'E':
                pos[0] += param
            elif instr[0] == 'W':
                pos[0] -= param
        elif instr[0] in ['F']:
            if dir == 0:
                pos[0] += param
            elif dir == 180:
                pos[0] -= param
            elif dir == 90:
                pos[1] += param
            elif dir == 270:
                pos[1] -= param
            else:
                print('Error: unknown direction', dir)
                exit()
        else:
            print('Error: unknown instruction', instr)
            exit()
    return abs(pos[0])+abs(pos[1])

def part2(data = False):
    if not data:
        data = read_input('input')
    ship_pos = [0,0]
    wayp_pos = [10,1]
    for instr in data:
        param = int(instr[1:])
        if instr[0] in ['L','R']:
            wp = wayp_pos.copy()
            if instr[0] == 'L':
                wayp_pos = rotate_quick(wp, param)
            else:
                wayp_pos = rotate_quick(wp, param, -1)
        elif instr[0] in ['N','S','E','W']:
            if instr[0] == 'N':
                wayp_pos[1] += param
            elif instr[0] == 'S':
                wayp_pos[1] -= param
            elif instr[0] == 'E':
                wayp_pos[0] += param
            elif instr[0] == 'W':
                wayp_pos[0] -= param
        elif instr[0] in ['F']:
            ship_pos[0] += wayp_pos[0] * param
            ship_pos[1] += wayp_pos[1] * param
        else:
            print('Error: unknown instruction', instr)
            exit()
    return abs(ship_pos[0])+abs(ship_pos[1])


def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 25
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert part2(data) == 286
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
data = read_input('input')
