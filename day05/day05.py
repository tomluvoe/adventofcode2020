#!/usr/bin/python3

import re

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def calculate_row(data):
    row = [0, 127]
    for i in range(7):
        row[0] = row[0] + 2**(6-i) if data[i] == 'B' else row[0]
        row[1] = row[1] - 2**(6-i) if data[i] == 'F' else row[1]
    #print(row)
    return row[0]

def calculate_col(data):
    col = [0, 7]
    for i in range(3):
        col[0] = col[0] + 2**(2-i) if data[i] == 'R' else col[0]
        col[1] = col[1] - 2**(2-i) if data[i] == 'L' else col[1]
    #print(col)
    return col[0]

def calculate_seat_id(data):
    row = calculate_row(data[0:7])
    col = calculate_col(data[7:10])
    return row * 8 + col

def part1(data = False):
    if not data:
        data = read_input('input')
    max_seat_id = 0
    for boarding_pass in data:
        seat_id = calculate_seat_id(boarding_pass)
        max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id
    return max_seat_id

def part2(data = False):
    if not data:
        data = read_input('input')
    my_seat_id = []
    seat_id_list = []
    for boarding_pass in data:
        seat_id_list.append(calculate_seat_id(boarding_pass))
    my_seat_id.extend(range(min(seat_id_list),max(seat_id_list)+1))
    for seat_id in seat_id_list:
        #print(seat_id)
        my_seat_id.remove(seat_id)
    return my_seat_id[0]

def unit_test_p1():
    print("Unit test start:")
    assert calculate_seat_id('BFFFBBFRRR') == 567
    print("Test 1 OK")
    assert calculate_seat_id('FFFBBBFRRR') == 119
    print("Test 2 OK")
    assert calculate_seat_id('BBFFBBFRLL') == 820
    print("Test 3 OK")

def unit_test_p2():
    print("Unit test start:")
    print("Test 1 OK")
    print("No test defined..")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
