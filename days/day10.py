#!/usr/bin/env python
import time


def part1(data):
    lines = data.strip().splitlines()
    rc,rx = 0, 1
    ans = 0
    def cycle():
        nonlocal ans, rc, rx
        rc += 1
        if (rc + 20) % 40 == 0:
            ans += rx * rc
    for line in lines:
        match line.split():
            case 'noop',:
                cycle()
            case 'addx', n:
                cycle()
                cycle()
                rx += int(n)
    return ans


def part2(data):
    lines = data.strip().splitlines()
    grid = set()
    rc,rx,ry,sw = 0, 1, 0, 40
    def cycle():
        nonlocal rc, ry
        for x in range(rx-1, rx+2):
            if x == rc % sw:
                grid.add((x,ry))
        rc += 1
        ry += rc % sw == 0
    for line in lines:
        match line.split():
            case 'noop',:
                cycle()
            case 'addx', n:
                cycle()
                cycle()
                rx += int(n)
    ans = '\n' + display(grid).rstrip('\n')
    return ans


def display(grid):
    minx,maxx = min(x for x,y in grid), max(x for x,y in grid)
    miny,maxy = min(y for x,y in grid), max(y for x,y in grid)
    so = ''
    for y in range(miny, maxy+1):
        a = ['.#'[(x,y) in grid] for x in range(minx, maxx+1)]
        so += ''.join(a) + '\n'
    return so


data = r'''
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''
assert part1(data) == 13140

expect = r'''
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....'''
assert part2(data) == expect


data = open('day10.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
