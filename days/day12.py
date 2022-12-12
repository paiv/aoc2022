#!/usr/bin/env python
from collections import deque


def solve(data, batch):
    lines = data.strip().splitlines()
    grid = {(x+1j*y):ord(c) for y,s in enumerate(lines) for x,c in enumerate(s)}
    neib = [1, -1, 1j, -1j]
    A,Z,S,E,ff = map(ord, 'azSE\xff')
    S = next(p for p,c in grid.items() if c == S)
    E = next(p for p,c in grid.items() if c == E)
    grid[S] = A
    grid[E] = Z
    fringe = deque([(p, 0) for p,c in grid.items() if c == A if batch or p == S])
    seen = set()
    while fringe:
        p, w = fringe.popleft()
        if p == E: return w
        if p in seen: continue
        seen.add(p)
        for s in neib:
            q = p + s
            if grid.get(q, ff) - grid[p] < 2:
                fringe.append((q, w+1))


def part1(data): return solve(data, batch=False)
def part2(data): return solve(data, batch=True)


data = r'''
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
assert part1(data) == 31
assert part2(data) == 29


data = open('day12.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
