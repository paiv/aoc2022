#!/usr/bin/env python
import itertools
import time


def part1(data, N=2022):
    input = itertools.cycle(data.strip())
    shapes = [{0,1,2,3}, {1,1j,1+1j,2+1j,1+2j}, {0,1,2,2+1j,2+2j}, {0,1j,2j,3j}, {0,1,1j,1+1j}]
    grid = set()
    minx, maxx, maxy = 0, 6, -1
    si = 0
    for t in range(N):
        pos = 2 + 1j * (maxy+4)
        shape = {k+pos for k in shapes[si]}
        # display(grid, shape)
        for c in input:
            if c == '<' and all((k.real > 0) and (k-1 not in grid) for k in shape):
                shape = {k-1 for k in shape}
            elif c == '>' and all((k.real < 6) and (k+1 not in grid) for k in shape):
                shape = {k+1 for k in shape}
            if any((k.imag == 0) or (k-1j in grid) for k in shape):
                grid.update(shape)
                maxy = max(maxy, max(int(k.imag) for k in shape))
                si = (si + 1) % len(shapes)
                break
            else:
                shape = {k-1j for k in shape}
            # display(grid, shape)
    # display(grid)
    ans = maxy+1
    return ans


def display(grid, shape=None):
    shape = shape or {}
    minx,maxx = 0, 6
    miny,maxy = 0, max(k.imag for k in (grid or {0}))+7
    so = ''
    for y in reversed(range(int(miny), int(maxy)+1)):
        so += ''.join('@' if p in shape else '.#'[p in grid] for x in range(int(minx), int(maxx)+1) for p in [x+1j*y]) + '\n'
    print(so)
    time.sleep(0.5)


def part2(data, N=1000000000000):
    def period():
        shapes = [{0,1,2,3}, {1,1j,1+1j,2+1j,1+2j}, {0,1,2,2+1j,2+2j}, {0,1j,2j,3j}, {0,1,1j,1+1j}]
        cn = len(data.strip())
        sn = len(shapes)
        input = enumerate(itertools.cycle(data.strip()))
        shapes = enumerate(itertools.cycle(shapes))
        grid = set()
        minx, maxx, maxy = 0, 6, -1
        seen = dict()
        stats = dict()
        for t in itertools.count():
            pos = 2 + 1j * (maxy+4)
            si,shape = next(shapes)
            shape = {k+pos for k in shape}
            for ci,c in input:
                if c == '<' and all((k.real > 0) and (k-1 not in grid) for k in shape):
                    shape = {k-1 for k in shape}
                elif c == '>' and all((k.real < 6) and (k+1 not in grid) for k in shape):
                    shape = {k+1 for k in shape}
                if any((k.imag == 0) or (k-1j in grid) for k in shape):
                    grid.update(shape)
                    maxy = max(maxy, max(int(k.imag) for k in shape))
                    state = f'{si%sn}:{ci%cn}:' + ''.join('.#'[(x+1j*y) in grid] for y in range(maxy-1, maxy+1) for x in range(7))
                    if (n := seen.get(state, 0)) == 2:
                        s,v = stats[state]
                        return s, t-s, maxy - v
                    else:
                        seen[state] = n + 1
                        stats[state] = (t, maxy)
                    break
                else:
                    shape = {k-1j for k in shape}

    s,p,h = period()
    a = (N - s) // p * h
    b = part1(data, s + (N - s) % p)
    ans = a + b
    return ans


data = r'''
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''
assert part1(data) == 3068
assert part2(data) == 1514285714288


data = open('day17.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
