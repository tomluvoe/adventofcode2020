#!/usr/bin/python3

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def next_bus_and_wait_time(timestamp, bus_list):
    bus_ids = []
    wait_time = []
    timestamp = int(timestamp)
    for bus in bus_list:
        if bus == 'x':
            continue
        else:
            bus = int(bus)
            bus_ids.append(bus)
            wait_time.append(int(round((1+timestamp//bus-timestamp/bus)*bus)))
    id = wait_time.index(min(wait_time))
    return bus_ids[id], wait_time[id]

def find_delta_time_multiple(now, step, bus, delta):
    multiple_found = False
    while not multiple_found:
        if (now + delta) % bus == 0:
            multiple_found = True
        else:
            now += step
    step *= bus
    return now, step

def part1(data = False):
    timestamp = 0
    bus_ids = ''
    if not data:
        timestamp,bus_ids = read_input('input')
    else:
        timestamp,bus_ids = data
    bus_list = bus_ids.split(',')
    bus_id, wait = next_bus_and_wait_time(timestamp, bus_list)
    return bus_id * wait

def part2(data = False):
    bus_ids = ''
    if not data:
        timestamp,bus_ids = read_input('input')
    else:
        timestamp,bus_ids = data
    bus_list = bus_ids.split(',')
    step = now = int(bus_list[0])
    for delta,bus in enumerate(bus_list[1:]):
        if not bus == 'x':
            now, step = find_delta_time_multiple(now, step, int(bus), delta+1)
    return now

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 295
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert part2(data) == 1068781
    print("Test 1 OK")
    data = read_input('test_input_2')
    for i,test_d in enumerate(data):
        data_str, result = test_d.split('=')
        assert part2(['0',data_str]) == int(result)
        print("Test",i+2,"OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
