#!/usr/bin/env python
import math
import re
import time


def part1(data):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    amap,ops = data.strip('\n').split('\n\n')
    lines = amap.strip('\n').splitlines()
    grid = {(x+1j*y):c for y,s in enumerate(lines) for x,c in enumerate(s) if not c.isspace()}
    limits = [[x for x,c in enumerate(s) if not c.isspace()] for y,s in enumerate(lines)]
    limits = [range(min(r), max(r)+1) for r in limits]
    minx,miny = min(p.real for p in grid), min(p.imag for p in grid)
    maxx,maxy = max(p.real for p in grid), max(p.imag for p in grid)
    limitsy = dict()
    for x in range(int(minx), int(maxx)+1):
        ys = [y for y in range(int(miny), int(maxy)+1) if (x+1j*y) in grid]
        limitsy[x] = range(min(ys), max(ys)+1) if ys else range(0)

    pos = limits[0].start + 1j * miny
    dir = 1
    for op in re.findall(r'L|R|\d+', ops):
        match op:
            case 'L': dir *= -1j
            case 'R': dir *= 1j
            case n:
                for _ in range(int(n)):
                    p = pos + dir
                    if p in grid:
                        if grid[p] == '#':
                            break
                        pos = p
                    else:
                        match dir:
                            case 1:
                                x = limits[int(pos.imag)].start
                                p = x + 1j*pos.imag
                            case -1:
                                x = limits[int(pos.imag)].stop-1
                                p = x + 1j*pos.imag
                            case 1j:
                                y = limitsy[int(pos.real)].start
                                p = pos.real + 1j * y
                            case -1j:
                                y = limitsy[int(pos.real)].stop-1
                                p = pos.real + 1j * y
                        if grid[p] == '#':
                            break
                        pos = p

    ans = int((pos.imag + 1) * 1000 + (pos.real+1) * 4) + [1,1j,-1,-1j].index(dir)
    return ans


def part2(data):
    board,ops = data.strip('\n').split('\n\n')
    lines = board.strip('\n').splitlines()
    S = math.gcd(*map(len, lines))
    grid = {(x+1j*y):c for y,s in enumerate(lines) for x,c in enumerate(s) if not c.isspace()}
    def face(pos): return (pos.real // S + pos.imag // S * 1j)
    def make_jumps(faces):
        res = dict()
        for a in faces:
            for s in [1,-1,1j,-1j]:
                if (b := a + s) in faces:
                    res[a,s] = (1,0,s)
                    res[b,-s] = (1,0,-s)
        #             for t in (s*1j, -s*1j):
        #                 if (c := b + t) in faces and (a + t) not in faces:
        #                     res[a,t] = (,s)
        if 1 in faces:
            '''
             45
             6
            23
            1
            '''
            # 4 - 1
            res[1+0j,-1j] = (1j, S*(0+2j)-1, 1)
            res[0+3j,-1] = (-1j, -S*(2+0j)-1j, 1j)
            # 5 - 1
            res[2+0j,-1j] = (1, -S*(2-4j), -1j)
            res[0+3j,1j] = (1, S*(2-4j), 1j)
            # 4 - 2
            res[1+0j,-1] = (-1, S*(1+3j)-(1+1j), 1)
            res[0+2j,-1] = (-1, S*(1+3j)-(1+1j), 1)
            # 5 - 3
            res[2+0j,1] = (-1, S*(5+3j)-(1+1j), -1)
            res[1+2j,1] = (-1, S*(5+3j)-(1+1j), -1)
            # 5 - 6
            res[2+0j,1j] = (1j, S*(3-1j)-1, -1)
            res[1+1j,1] = (-1j, S*(1+3j)-1j, -1j)
            # 6 - 2
            res[1+1j,-1] = (-1j, S*(-1+3j)-1j, 1j)
            res[0+2j,-1j] = (1j, S*(3+1j)-1, 1)
            # 1 - 3
            res[0+3j,1] = (-1j, S*(-2+4j)-1j, -1j)
            res[1+2j,1j] = (1j, S*(4+2j)-1, -1)
        else:
            res[1+1j,-1j] = (1j, S*(3-1j)-1, 1)
            res[2+1j,1] = (1j, S*(5-1j)-1, 1j)
            res[2+2j,1j] = (-1, S*(3+5j)-(1+1j), -1j)
        return res
    faces = {face(p) for p in grid}
    jumps = make_jumps(faces)
    def step(pos, dir):
        s = pos + dir
        fp, fs = face(pos), face(s)
        if fp == fs: return (s, dir)
        k,m,d = jumps[fp,dir]
        return s*k+m, d
    pos = lines[0].index('.')
    dir = 1
    for op in re.findall(r'L|R|\d+', ops):
        match op:
            case 'L': dir *= -1j
            case 'R': dir *= 1j
            case n:
                for _ in range(int(n)):
                    s,d = step(pos, dir)
                    if s not in grid:
                        print(pos, face(pos), dir, s, d)
                    if grid[s] == '#':
                        break
                    pos,dir = s,d

    ans = int(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + [1,1j,-1,-1j].index(dir))
    return ans


def display(grid, pos, dir):
    minx,maxx = min(int(p.real) for p in grid), max(int(p.real) for p in grid)
    miny,maxy = min(int(p.imag) for p in grid), max(int(p.imag) for p in grid)
    c = {1:'>', -1:'<', 1j:'v', -1j:'^'}[dir]
    so = ''
    for y in range(miny, maxy+1):
        a = [grid.get(x+1j*y, ' ') for x in range(minx, maxx+1)]
        if pos.imag == y:
            a[int(pos.real-minx)] = c
        so += ''.join(a) + '\n'
    print(so)
    time.sleep(0.5)


data = r'''
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''
assert part1(data) == 6032
assert part2(data) == 5031


data = open('day22.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
