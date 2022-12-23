#!/usr/bin/env python
from collections import defaultdict


def evolve(data, T=1000000):
    lines = data.strip().splitlines()
    grid = {(x+1j*y) for y,s in enumerate(lines) for x,c in enumerate(s) if c == '#'}
    neib = [1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j]
    props = [[-1-1j, -1j, 1-1j], [-1+1j, 1j, 1+1j], [-1-1j, -1, -1+1j], [1-1j, 1, 1+1j]]
    props += props
    state = 0
    # display(grid)
    for t in range(1, T+1):
        claims = defaultdict(int)
        dawn = dict()
        for p in grid:
            dawn[p] = p
            if any((p+s) in grid for s in neib):
                for ms in props[state:state+4]:
                    if all((p+s) not in grid for s in ms):
                        s = p + ms[1]
                        claims[s] += 1
                        dawn[p] = s
                        break
        state = (state + 1) % 4
        day = {s if claims[s] == 1 else p for p,s in dawn.items()}
        if day == grid: break
        grid = day
        # print(t)
        # display(grid)

    return (grid,t)


def display(grid):
    minx,maxx = min(int(p.real) for p in grid), max(int(p.real) for p in grid)
    miny,maxy = min(int(p.imag) for p in grid), max(int(p.imag) for p in grid)
    so = ''
    for y in range(miny-1, maxy+2):
        so += ''.join('.#'[(x+1j*y) in grid] for x in range(minx-1, maxx+2)) + '\n'
    print(so)


def part1(data):
    grid,t = evolve(data, T=10)
    ans = 0
    minx,maxx = min(int(p.real) for p in grid), max(int(p.real) for p in grid)
    miny,maxy = min(int(p.imag) for p in grid), max(int(p.imag) for p in grid)
    for y in range(miny, maxy+1):
        ans += sum((x+1j*y)not in grid for x in range(minx, maxx+1))
    return ans


def part2(data):
    grid,t = evolve(data)
    return t


data = r'''
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
'''
assert part1(data) == 110
assert part2(data) == 20


data = open('day23.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
