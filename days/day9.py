#!/usr/bin/env python
import time


def display(ps):
    grid = {(x,y) for x,y in ps}
    minx,maxx = min(x for x,y in ps), max(x for x,y in ps)
    miny,maxy = min(y for x,y in ps), max(y for x,y in ps)
    hx,hy = ps[0]
    fx,fy = 10-min(10, maxx - minx), 5-min(5, maxy - miny)
    minx -= fx
    maxx += fx
    miny -= fy
    maxy += fy
    so = ''
    for y in range(miny, maxy+1):
        a = [' #'[(x,y) in grid] for x in range(minx, maxx+1)]
        if y == hy:
            a[hx-minx] = '@'
        so += ''.join(a) + '\n'
    print(so)
    time.sleep(0.3)


def part1(data, N=2):
    def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
    lines = data.strip().splitlines()
    seen = set()
    ps = [(0,0) for _ in range(N)]
    def chace(p, q):
        px,py = p
        qx,qy = q
        dx,dy = qx-px, qy-py
        if abs(dx) > 1 or abs(dy) > 1:
            if dx: px += sign(dx)
            if dy: py += sign(dy)
        return (px,py)
    for line in lines:
        match line.split():
            case 'R', n: dx,dy = 1,0
            case 'L', n: dx,dy = -1,0
            case 'D', n: dx,dy = 0,1
            case 'U', n: dx,dy = 0,-1
            case _: raise Exception(line)
        for _ in range(int(n)):
            px,py = ps[0]
            ps[0] = (px+dx, py+dy)
            for i in range(N-1):
                ps[i+1] = chace(ps[i+1], ps[i])
            seen.add(ps[-1])
            # display(ps)
    ans = len(seen)
    return ans


def part1(data, N=2):
    def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
    def cign(c): return sign(c.real) + 1j * sign(c.imag)
    lines = data.strip().splitlines()
    seen = set()
    ps = [0j for _ in range(N)]
    def chace(p, q):
        dx,dy = q.real - p.real, q.imag - p.imag
        if abs(dx) > 1 or abs(dy) > 1:
            p += cign(q - p)
        return p
    for line in lines:
        match line.split():
            case 'R', n: d = 1
            case 'L', n: d = -1
            case 'D', n: d = 1j
            case 'U', n: d = -1j
        for _ in range(int(n)):
            ps[0] += d
            for i in range(N-1):
                ps[i+1] = chace(ps[i+1], ps[i])
            seen.add(ps[-1])
    ans = len(seen)
    return ans


def part2(data): return part1(data, N=10)


data = r'''
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
assert part1(data) == 13
assert part2(data) == 1

data = r'''
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''
assert part2(data) == 36


data = open('day9.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
