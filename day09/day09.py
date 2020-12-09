#!/usr/bin/python3

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def is_sum(preamble, number):
    is_valid = False
    for i in range(len(preamble)):
        for j in range(i+1,len(preamble)):
            if int(number) == int(preamble[i]) + int(preamble[j]):
                is_valid = True
                break
        if is_valid:
            break
    return is_valid

def contiguous_sum(preamble, number):
    preamble = [int(n) for n in preamble]
    c_sum = 0
    for i in range(len(preamble)):
        j = i + 1
        sum = int(preamble[i])
        while j < len(preamble) and sum < number:
            sum += int(preamble[j])
            j += 1
        if sum == number:
            c_sum = int(max(preamble[i:j])) + int(min(preamble[i:j]))
            break
    return c_sum

def first_xmas_error(data, preamble_size=25, ret_list=False):
    is_valid = True
    num = int(data[0])
    ret_data = []
    for i in range(len(data)-preamble_size):
        preamble = data[i:preamble_size+i]
        ret_data = data[0:preamble_size+i]
        input = data[preamble_size+i:]
        is_valid = is_sum(preamble, input[0])
        if not is_valid:
            num = int(input[0])
            break
    if ret_list:
        return ret_data
    return num

def part1(data = False):
    if not data:
        data = read_input('input')
    return first_xmas_error(data)

def part2(data = False):
    if not data:
        data = read_input('input')
    number = first_xmas_error(data)
    data_list = first_xmas_error(data, ret_list=True)
    return contiguous_sum(data_list, number)

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    preamble = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    assert is_sum(preamble,26) == True
    print("Test 1 OK")
    assert is_sum(preamble,49) == True
    print("Test 2 OK")
    assert is_sum(preamble,100) == False
    print("Test 3 OK")
    assert is_sum(preamble,50) == False
    print("Test 4 OK")
    preamble_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,45,21,22,23,24,25]
    assert is_sum(preamble_2,26) == True
    print("Test 5 OK")
    assert is_sum(preamble_2,65) == False
    print("Test 6 OK")
    assert is_sum(preamble_2,64) == True
    print("Test 7 OK")
    assert is_sum(preamble_2,66) == True
    print("Test 8 OK")
    assert first_xmas_error(data, 5) == 127
    print("Test 9 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert contiguous_sum(data, 127) == 62
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
