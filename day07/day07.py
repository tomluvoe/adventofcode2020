#!/usr/bin/python3

import re

def read_input(input_file):
    with open(input_file, 'r') as input_file:
        data = input_file.read()[:-1]
    data = data.split('\n')
    return data

def _parse_rule(rule):
    ma = re.search(r'([a-z ]+) bags contain (.+).', rule)
    outer = ma.group(1)
    rule_dict = { outer: {} }
    contains = ma.group(2).split(', ')
    for bags in contains:
        if bags != 'no other bags':
            ma = re.search(r'([0-9]+) (.+) bag\.?', bags)
        else:
            continue
        if ma.group(1).isdigit():
            rule_dict[outer][ma.group(2)] = int(bags[0])
    return rule_dict

def _parse_rule_inv(rule):
    ma = re.search(r'([a-z ]+) bags contain (.+).', rule)
    outer = ma.group(1)
    rule_dict_inv = {}
    contains = ma.group(2).split(', ')
    for bags in contains:
        if bags != 'no other bags':
            ma = re.search(r'([0-9]+) (.+) bag\.?', bags)
        else:
            continue
        if ma.group(1).isdigit():
            rule_dict_inv[ma.group(2)] = { 'outer': outer }
    return rule_dict_inv

def parse_rules(data, inv=True):
    rules_list = []
    for rule in data:
        rules = {}
        if inv:
            rules = _parse_rule_inv(rule)
        else:
            rules = _parse_rule(rule)
        if rules != {}:
            rules_list.append(rules)
    return rules_list

def _bag_colors_contains(bag_color, rules_list, all=False):
    bag_list = []
    for rule in rules_list:
        for key in rule.keys():
            if bag_color == key:
                if not all:
                    bag_list.append(rule[key]['outer'])
                else:
                    for inner_bag in rule[key].keys():
                        bag_list.extend([inner_bag]*rule[key][inner_bag])
    return bag_list

def how_many_bag_colors(bag_color, rules_list):
    bag_color_list = [bag_color]
    id = 0
    while len(bag_color_list) > id:
        bag_color_list.extend(_bag_colors_contains(bag_color_list[id], rules_list))
        id += 1
    number_of_bags = len(list(dict.fromkeys(bag_color_list[1:])))
    return number_of_bags

def how_many_bags_list(bag_color, rules_list):
    bag_color_list = [bag_color]
    id = 0
    while len(bag_color_list) > id:
        bag_color_list.extend(_bag_colors_contains(bag_color_list[id], rules_list, all=True))
        id += 1
    return bag_color_list[1:]

def part1(data = False):
    if not data:
        data = read_input('input')
    rules_list = parse_rules(data)
    number_of_bags = how_many_bag_colors('shiny gold', rules_list)
    return number_of_bags

def part2(data = False):
    if not data:
        data = read_input('input')
    rules_list = parse_rules(data, inv=False)
    bag_list = how_many_bags_list('shiny gold', rules_list)
    return len(bag_list)

def unit_test_p1():
    data = read_input('test_input')
    print("Unit test start:")
    assert part1(data) == 4
    print("Test 1 OK")

def unit_test_p2():
    data = read_input('test_input')
    print("Unit test start:")
    assert part2(data) == 32
    print("Test 1 OK")
    data = read_input('test_input_2')
    assert part2(data) == 126
    print("Test 2 OK")

print("** Part one")
unit_test_p1()
print("My solution is: ", part1(), "\n")

print("** Part two")
unit_test_p2()
print("My solution is:", part2(), "\n")
