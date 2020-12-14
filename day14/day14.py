#!/usr/bin/python3

import re

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def exec_instr(mask, memory, instr, mad=False):
    cmd, value = instr.split(' = ')
    out = [0]*len(mask)
    if cmd == 'mask':
        mask = value
    elif cmd[:3] == 'mem':
        if not mad:
            ma = re.search(r'mem\[([0-9]+)\]', cmd)
            addr = int(ma.group(1))
            bval = format(int(value), 'b')
            bval = '0'*(len(mask)-len(bval)) + bval
            for i in range(len(bval)):
                if mask[i] == 'X':
                    out[i] = bval[i]
                else:
                    out[i] = mask[i]
            memory[addr] = int(''.join(out), 2)
        else:
            ma = re.search(r'mem\[([0-9]+)\]', cmd)
            addr = format(int(ma.group(1)),'b')
            addr = '0'*(len(mask)-len(addr))+addr
            addr_mask = ['0']*len(mask)
            for i in range(len(addr)):
                if mask[i] == '0':
                    addr_mask[i] = addr[i]
                else:
                    addr_mask[i] = mask[i]
            addr_list = []
            for i in range(2**mask.count('X')):
                dstr = format(i, 'b')
                dstr = '0'*(mask.count('X')-len(dstr))+dstr
                j = 0
                addr_tmp = []
                for a in addr_mask:
                    if a == 'X':
                        addr_tmp.append(dstr[j])
                        j += 1
                    else:
                        addr_tmp.append(a)
                memory[int(''.join(addr_tmp),2)] = int(value)
    return mask, memory

def part1(data = False):
    if not data:
        data = read_input('input')
    mask =   "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}
    for instr in data:
        mask, memory = exec_instr(mask, memory, instr)
    rv = 0
    for key in memory:
        rv += memory[key]
    return rv

def part2(data = False):
    if not data:
        data = read_input('input')
    mask =   "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}
    for instr in data:
        mask, memory = exec_instr(mask, memory, instr, mad=True)
    rv = 0
    for key in memory:
        rv += memory[key]
    return rv

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 165
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input_2')
    print("Unit test start:")
    assert part2(data) == 208
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
