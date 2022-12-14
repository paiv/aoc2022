#!/usr/bin/env python
import re


def parse(data):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
    grid = dict()
    data = [ints(s) for s in data.strip().splitlines()]
    maxy = 0
    for line in data:
        for ax,ay,bx,by in (line[i:i+4] for i in range(0, len(line)-3, 2)):
            dx,dy = sign(bx - ax), sign(by - ay)
            x,y = ax,ay
            for _ in range(abs(by-ay)+1):
                for _ in range(abs(bx-ax)+1):
                    grid[(x,y)] = 1
                    maxy = max(maxy, y)
                    x += dx
                    y += dy
    return grid, maxy


def part1(data):
    grid, maxy = parse(data)
    S = len(grid)
    while True:
        x,y = 500,0
        while y <= maxy:
            if not grid.get((x, y+1)):
                y += 1
            elif not grid.get((x-1, y+1)):
                x -= 1
                y += 1
            elif not grid.get((x+1, y+1)):
                x += 1
                y += 1
            else:
                grid[(x,y)] = 2
                break
        else:
            ans = len(grid) - S
            return ans


def part2(data):
    grid, maxy = parse(data)
    S = len(grid)
    while not grid.get((500,0)):
        x,y = 500,0
        while y <= maxy:
            if not grid.get((x, y+1)):
                y += 1
            elif not grid.get((x-1, y+1)):
                x -= 1
                y += 1
            elif not grid.get((x+1, y+1)):
                x += 1
                y += 1
            else:
                grid[(x,y)] = 2
                break
        else:
            grid[(x,y)] = 2
    ans = len(grid) - S
    return ans


data = r'''
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''
assert part1(data) == 24
assert part2(data) == 93


data = open('day14.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
