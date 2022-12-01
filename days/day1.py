#!/usr/bin/env python


def part1(data):
    bags = list()
    for s in data.strip().split('\n\n'):
        bags.append(sum(map(int, s.split())))
    ans = max(bags)
    return ans


def part2(data):
    bags = list()
    for s in data.strip().split('\n\n'):
        bags.append(sum(map(int, s.split())))
    ans = sum(sorted(bags)[-3:])
    return ans


data = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
assert part1(data) == 24000
assert part2(data) == 45000


data = open('day1.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
