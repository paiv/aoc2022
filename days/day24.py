#!/usr/bin/env python
import heapq
import math
from collections import deque
from functools import cache


def walk(data, T0=0, back=False):
    lines = data.strip().splitlines()
    W,H = len(lines[0]), len(lines)
    start = complex(lines[0].index('.'),0)
    goal = complex(lines[-1].index('.'),H-1)
    grid = {complex(x,y) for y,s in enumerate(lines) for x,c in enumerate(s) if c != '#'}
    neib = [1,-1,1j,-1j]
    winds = {complex(x,y):neib['><v^'.index(c)] for y,s in enumerate(lines) for x,c in enumerate(s) if c in '><^v'}
    M = math.lcm((W-2), (H-2))
    if back:
        start,goal = goal,start

    @cache
    def forecast(t):
        return {complex((p.real-1+t*s.real)%(W-2)+1, (p.imag-1+t*s.imag)%(H-2)+1) for p,s in winds.items()}

    def valid(t, pos):
        return (pos in grid) and (pos not in forecast(t % M))

    neib = [1,-1,1j,-1j]
    fringe = deque([(T0, start)])
    seen = set()
    while fringe:
        t,p = fringe.popleft()
        if p == goal:
            ans = t
            break
        k = (t,p)
        if k in seen: continue
        seen.add(k)
        for s in neib:
            q = p + s
            if valid(t+1, q) and q != start:
                fringe.append((t+1, q))
        if valid(t+1, p):
                fringe.append((t+1, p))

    return ans


def walk(data, T0=0, back=False):
    lines = data.strip().splitlines()
    W,H = len(lines[0]), len(lines)
    start = lines[0].index('.'),0
    goal = lines[-1].index('.'),H-1
    grid = {(x,y) for y,s in enumerate(lines) for x,c in enumerate(s) if c != '#'}
    neib = [(1,0), (-1,0), (0,1), (0,-1)]
    winds = {(x,y):neib['><v^'.index(c)] for y,s in enumerate(lines) for x,c in enumerate(s) if c in '><^v'}
    M = math.lcm((W-2), (H-2))
    if back:
        start,goal = goal,start

    def dist(a,b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @cache
    def forecast(t):
        return {((x-1+t*dx)%(W-2)+1, (y-1+t*dy)%(H-2)+1) for (x,y),(dx,dy) in winds.items()}

    def valid(t, pos):
        return (pos in grid) and (pos not in forecast(t % M))

    fringe = [(dist(start,goal), T0, start)]
    seen = set()
    while fringe:
        w,t,p = heapq.heappop(fringe)
        if p == goal:
            ans = t
            break
        px,py = p
        k = (t,py,px)
        if k in seen: continue
        seen.add(k)
        for sx,sy in neib:
            q = (px+sx, py+sy)
            if valid(t+1, q) and q != start:
                heapq.heappush(fringe, (t+1+dist(q,goal), t+1, q))
        if valid(t+1, p):
            heapq.heappush(fringe, (w+1, t+1, p))
    return ans


def part1(data):
    ans = walk(data, T0=0)
    return ans


def part2(data):
    t1 = walk(data, T0=0, back=False)
    t2 = walk(data, T0=t1, back=True)
    ans = walk(data, T0=t2, back=False)
    return ans


data = r'''
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''
assert part1(data) == 18
assert part2(data) == 54


data = open('day24.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
