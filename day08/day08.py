#!/usr/bin/python3

import re
import copy

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def prep_code(data):
    code = []
    for d in data:
        ma = re.search(r'([a-z]+) (.+)', d)
        code.append([ma.group(1), int(ma.group(2))])
    return code

def parse_instr(out, instr):
    rt = 0
    if out == 'pc' and instr[0] in ('nop','jmp','acc'):
        rt = instr[1] if instr[0] == 'jmp' else 1
    if out == 'acc' and instr[0] in ('acc'):
        rt = instr[1]
    return rt

def find_change_list(data):
    change_list = []
    for i,d in enumerate(data):
        if d[0] == 'nop':
            change_list.append([i, 'jmp'])
        elif d[0] == 'jmp':
            change_list.append([i, 'nop'])
    return change_list

def patch_code(change, orig_code):
    code = orig_code[:]
    code[change[0]][0] = change[1]
    return code

def part1(data = False):
    if not data:
        data = read_input('input')
    code = prep_code(data)
    pc = 0
    acc = 0
    pc_list = [pc]
    while 0 <= pc < len(data):
        acc += parse_instr('acc', code[pc])
        pc += parse_instr('pc', code[pc])
        if pc in pc_list:
            break
        pc_list.append(pc)
    return acc

def part2(data = False):
    if not data:
        data = read_input('input')
    orig_code = prep_code(data)
    change_list = find_change_list(orig_code)
    success = False
    while not success:
        pc = 0
        acc = 0
        pc_list = [pc]
        code = patch_code(change_list[0], copy.deepcopy(orig_code))
        change_list = change_list[1:]
        while 0 <= pc < len(data):
            acc += parse_instr('acc', code[pc])
            pc += parse_instr('pc', code[pc])
            if pc in pc_list:
                break
            pc_list.append(pc)
        if pc == len(data):
            success = True
    return acc

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 5
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert part2(data) == 8
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
