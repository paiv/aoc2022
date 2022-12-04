#!/usr/bin/env python
import re


def part1(data):
    lines = data.strip().splitlines()
    ans = 0
    for line in lines:
        ax,ay,bx,by = list(map(int, re.findall(r'\d+', line)))
        ans += (bx <= ax <= by and bx <= ay <= by) or (ax <= bx <= ay and ax <= by <= ay)
    return ans



def part2(data):
    lines = data.strip().splitlines()
    ans = 0
    for line in lines:
        ax,ay,bx,by = list(map(int, re.findall(r'\d+', line)))
        ans += (ax <= bx and ay >= bx) or (bx <= ax and by >= ax)
    return ans


data = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
assert part1(data) == 2
assert part2(data) == 4


data = open('day4.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
