#!/usr/bin/env python
import string


def part1(data):
    wei = dict(zip(string.ascii_letters, range(1,53)))
    ans = 0
    for line in data.strip().splitlines():
        n = len(line)
        a,b = line[:n//2], line[n//2:]
        s = set(a) & set(b)
        ans += wei[s.pop()]
    return ans


def part2(data):
    wei = dict(zip(string.ascii_letters, range(1,53)))
    lines = data.strip().splitlines()
    ans = 0
    for a,b,c in (lines[i:i+3] for i in range(0, len(lines), 3)):
        s = set(a) & set(b) & set(c)
        ans += wei[s.pop()]
    return ans


data = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
assert part1(data) == 157
assert part2(data) == 70


data = open('day3.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
