#!/usr/bin/env python
import itertools
import re


def part1(data):
    gr, ops = data.split('\n\n')
    ops = [list(map(int, re.findall(r'-?\d+', s))) for s in ops.strip().splitlines()]
    crates = list()
    for line in gr.strip('\n').splitlines()[:-1]:
        s = [c for c,_ in re.findall(r' ?\[(\w)\]|  ( ) ', line)]
        crates.append(s)
    crates = [['']] + [list(filter(None, s)) for s in itertools.zip_longest(*crates)]
    for n,a,b in ops:
        ps = crates[a][:n][::-1]
        crates[a] = crates[a][n:]
        crates[b] = ps + crates[b]
    ans = ''.join(s[0] for s in crates)
    return ans


def part2(data):
    gr, ops = data.split('\n\n')
    ops = [list(map(int, re.findall(r'-?\d+', s))) for s in ops.strip().splitlines()]
    crates = list()
    for line in gr.strip('\n').splitlines()[:-1]:
        s = [c for c,_ in re.findall(r' ?\[(\w)\]|  ( ) ', line)]
        crates.append(s)
    crates = [['']] + [list(filter(None, s)) for s in itertools.zip_longest(*crates)]
    for n,a,b in ops:
        ps = crates[a][:n]
        crates[a] = crates[a][n:]
        crates[b] = ps + crates[b]
    ans = ''.join(s[0] for s in crates)
    return ans


data = '''
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
assert part1(data) == 'CMZ'
assert part2(data) == 'MCD'


data = open('day5.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
