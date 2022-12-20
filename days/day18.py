#!/usr/bin/env python
import re


def part1(data):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    def neib(x,y,z): return {(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)}
    cubes = {tuple(ints(s)) for s in data.strip().splitlines()}
    ans = sum(1 for p in cubes for s in neib(*p) - cubes)
    return ans


def part2(data):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    cubes = {tuple(ints(s)) for s in data.strip().splitlines()}
    def neib(x,y,z): return {(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)}
    a,b = min(min(p) for p in cubes), max(max(p) for p in cubes)
    ab = range(a-1, b+2)
    fringe = [(ab.start, ab.start, ab.start)]
    seen = set()
    while fringe:
        p = fringe.pop()
        if p in seen: continue
        seen.add(p)
        fringe += [s for s in neib(*p) - cubes if all(c in ab for c in s)]
    ans = sum(s in seen for p in cubes for s in neib(*p))
    return ans


data = r'''
1,1,1
2,1,1
'''
assert part1(data) == 10

data = r'''
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''
assert part1(data) == 64
assert part2(data) == 58


data = open('day18.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
