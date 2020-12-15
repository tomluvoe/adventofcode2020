#!/usr/bin/python3


def part1(data = False, loops=2021):
    if not data:
        exit()
    number_dict = {}
    for i in range(len(data)):
        number_dict[data[i]] = i+1
    number = data[-1]
    for turn in range(len(data)+1,loops):
        if number in number_dict:
            prev_turn = number_dict[number]
            number_dict[number] = turn - 1
            number = turn - 1 - prev_turn
        else:
            number_dict[number] = turn - 1
            number = 0
    return number

def part2(data = False):
    return part1(data,30000001)

def unit_test_p1():
    print("Unit test start:")
    assert part1([0,3,6]) == 436
    print("Test 1 OK")
    assert part1([1,3,2]) == 1
    print("Test 2 OK")
    assert part1([2,1,3]) == 10
    print("Test 3 OK")
    assert part1([1,2,3]) == 27
    print("Test 4 OK")
    assert part1([2,3,1]) == 78
    print("Test 5 OK")
    assert part1([3,2,1]) == 438
    print("Test 6 OK")
    assert part1([3,1,2]) == 1836
    print("Test 7 OK")

def unit_test_p2():
    pass
    #print("Unit test start:")
    #assert part2([0,3,6]) == 436
    #print("Test 1 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1([11,18,0,20,1,7,16]), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2([11,18,0,20,1,7,16]), "\n")
