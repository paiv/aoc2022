#!/usr/bin/env python


def part1(data):
    ans = 0
    for line in data.strip().splitlines():
        a,b = line.split()
        x = 'ABC'.index(a)
        y = 'XYZ'.index(b)
        ans += y + 1 + (y - x + 1) % 3 * 3
    return ans


def part2(data):
    ans = 0
    for line in data.strip().splitlines():
        a,b = line.split()
        x = 'ABC'.index(a)
        y = 'XYZ'.index(b)
        ans += (x + y - 1) % 3 + 1 + y * 3
    return ans


data = '''
A Y
B X
C Z
'''
assert part1(data) == 15
assert part2(data) == 12


data = open('day2.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
