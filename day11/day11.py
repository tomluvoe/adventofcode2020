#!/usr/bin/python3

import copy

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    for i,row in enumerate(data):
        data[i] = [ch for ch in row]
    return data

def read_input_raw(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    return data

def count_adjacent_occupied(row, col, data):
    count = 0
    for xy in list([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]):
        if row+xy[0] < 0 or col+xy[1] < 0 or row+xy[0] >= len(data) or col+xy[1] >= len(data[row]):
            continue
        if data[row+xy[0]][col+xy[1]] == '#':
            count += 1
    return count

def count_total_occupied_seats(data):
    return data.count('#')

def update_seat(i, rlen, data_list, data_ref, no_occupied=4):
    count = count_adjacent_occupied(i, rlen, data_ref)
    data_list[i] = '#' if (data_ref[i] == 'L' and count == 0) else data_list[i]
    data_list[i] = 'L' if (data_ref[i] == '#' and count >= no_occupied) else data_list[i]
    return data_list

def update_seat_visible(i, rlen, data_list, data_ref):
    count = count_visible_adjacent_occupied(i, rlen, data_ref)
    data_list[i] = '#' if (data_ref[i] == 'L' and count == 0) else data_list[i]
    data_list[i] = 'L' if (data_ref[i] == '#' and count >= 5) else data_list[i]
    return data_list

def count_adjacent_occupied(i, rlen, data):
    count = 0
    x = i%rlen
    y = int(i/rlen)
    for xy in list([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]):
        if x+xy[0] < 0 or y+xy[1] < 0 or x+xy[0] >= rlen or (y+xy[1])*rlen >= len(data):
            continue
        if data[(x+xy[0])+rlen*(y+xy[1])] == '#':
            count += 1
    return count

def count_visible_adjacent_occupied(i, rlen, data):
    count = 0
    x = i%rlen
    y = int(i/rlen)
    for dir in list([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]):
        step = 1
        found = False
        while not found:
            seat_pos = x+dir[0]*step + (y+dir[1]*step)*rlen
            if 0 <= x+dir[0]*step < rlen and 0 <= y+dir[1]*step < len(data)//rlen:
                if data[seat_pos] == '.':
                    step += 1
                else:
                    found = True
                    count += 1 if data[seat_pos] == '#' else 0
            else:
                found = True
    return count

def part1(data=False):
    if not data:
        data = read_input_raw('input')
    seat_updates = True
    rlen = data.find('\n')
    data = data.replace('\n','')
    while seat_updates:
        data_ref = copy.copy(data)
        occupied = count_total_occupied_seats(data)
        data_list = list(data)
        for i in range(len(data_list)):
            data = update_seat(i, rlen, data_list, data_ref)
        if occupied == count_total_occupied_seats(data):
            seat_updates = False
    return count_total_occupied_seats(data)

def part2(data=False):
    if not data:
        data = read_input_raw('input')
    seat_updates = True
    rlen = data.find('\n')
    data = data.replace('\n','')
    while seat_updates:
        data_ref = copy.copy(data)
        occupied = count_total_occupied_seats(data)
        data_list = list(data)
        for i, dat in enumerate(data):
            data_list = update_seat_visible(i, rlen, data_list, data_ref)
        data = ''.join(data_list)
        if occupied == count_total_occupied_seats(data):
            seat_updates = False
    return count_total_occupied_seats(data)

def unit_test_p1():
    print("Unit test start:")
    data = read_input_raw('test_input')
    assert part1(data) == 37
    print("Test 1 OK")

def unit_test_p2():
    data = read_input_raw('test_input_2')
    rlen = data.find('\n')
    data = data.replace('\n','')
    print("Unit test start:")
    assert count_visible_adjacent_occupied(39,rlen,data) == 8
    print("Test 1 OK")
    data = read_input_raw('test_input_3')
    rlen = data.find('\n')
    data = data.replace('\n','')
    assert count_visible_adjacent_occupied(24,rlen,data) == 0
    print("Test 2 OK")
    data = read_input_raw('test_input_4')
    rlen = 13
    data = data.replace('\n','')
    assert count_visible_adjacent_occupied(1,rlen,data) == 0
    print("Test 3 OK")
    data = read_input_raw('test_input')
    assert part2(data) == 26
    print("Test 4 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
