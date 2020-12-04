#!/usr/bin/python3

import re

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = [d.replace('\n',' ') for d in data.split('\n\n')]
    return data

def is_valid_passport(data):
    req_list = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    if all(req in data for req in req_list):
        return True
    return False

def _byr(data):
    #print('byr [1920,2002]',data,1920 <= int(data) <= 2002)
    return True if 1920 <= int(data) <= 2002 else False

def _iyr(data):
    #print('iyr [2010,2020]',data,2010 <= int(data) <= 2020)
    return True if 2010 <= int(data) <= 2020 else False

def _eyr(data):
    #print('eyr [2020,2030]',data,2020 <= int(data) <= 2030)
    return True if 2020 <= int(data) <= 2030 else False

def _hgt(data):
    rng = [150, 193]
    if 'in' in data:
        rng = [59, 76]
    if not data[:-2].isdigit():
        return False
    #print('hgt',rng,data,rng[0] <= int(data[:-2]) <= rng[1])
    return True if rng[0] <= int(data[:-2]) <= rng[1] else False

def _hcl(data):
    #print('hcl', data, data[0] == '#' and \
    #                len(data) == 7 and \
    #                re.match('^[A-Za-z0-9]*$', data[1:]))
    return True if data[0] == '#' and \
                    len(data) == 7 and \
                    re.match('^[A-Za-z0-9]*$', data[1:]) else False

def _ecl(data):
    #print('ecl',['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], data)
    return True if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] \
        else False

def _pid(data):
    #print('pid',data)
    return True if len(data) == 9 and data.isdigit() else False

func_mapping = {
    'byr': _byr,
    'iyr': _iyr,
    'eyr': _eyr,
    'hgt': _hgt,
    'hcl': _hcl,
    'ecl': _ecl,
    'pid': _pid
}

def passport_data_validation_ok(data):
    req_list = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for req in req_list:
        re_str = req + ':([a-zA-Z0-9#]+)'
        ma = re.search(r'{}'.format(re_str), data)
        #print(re_str)
        if ma:
            #print(ma.group(0))
            if not func_mapping[req](ma.groups()[0]):
                return False
        else:
            return False
    return True

def part1(data = False):
    count = 0
    if not data:
        data = read_input('input')
    for passport in data:
        count = count + 1 if is_valid_passport(passport) else count
    return count

def part2(data = False):
    count = 0
    if not data:
        data = read_input('input')
    for passport in data:
        #print('')
        #print(':passport:', passport)
        if is_valid_passport(passport):
            #print('OK')
            count = count + 1 if passport_data_validation_ok(passport) else count
            #print('passport validation: ',passport_data_validation_ok(passport))
        #else:
        #    print('NOK')
    return count

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 2
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input_2')
    print("Unit test start:")
    assert part2(data) == 4
    print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
