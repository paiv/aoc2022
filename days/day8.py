#!/usr/bin/env python


def part1(data):
    grid = [list(map(int, s)) for s in data.strip().splitlines()]
    w,h = len(grid[0]), len(grid)

    vis = set()
    for y in range(h):
        m = -1
        for x in range(w):
            n = grid[y][x]
            if n > m:
                vis.add((y,x))
                ox = x
                m = n
        m = -1
        for x in reversed(range(ox,w)):
            n = grid[y][x]
            if n > m:
                vis.add((y,x))
                ox = x
                m = n

    for x in range(w):
        m = -1
        for y in range(h):
            n = grid[y][x]
            if n > m:
                vis.add((y,x))
                oy = y
                m = n
        m = -1
        for y in reversed(range(oy,h)):
            n = grid[y][x]
            if n > m:
                vis.add((y,x))
                oy = y
                m = n

    ans = len(vis)
    return ans


def part2(data):
    grid = [list(map(int, s)) for s in data.strip().splitlines()]
    w,h = len(grid[0]), len(grid)

    def score(py, px):
        res = 1
        m = grid[py][px]
        for x in range(px+1, w):
            if grid[py][x] >= m: break
        res *= (x - px)
        for x in reversed(range(0, px)):
            if grid[py][x] >= m: break
        res *= (px - x)
        for y in range(py+1, h):
            if grid[y][px] >= m: break
        res *= (y - py)
        for y in reversed(range(0, py)):
            if grid[y][px] >= m: break
        res *= (py - y)
        return res

    ans = 0
    for y in range(1, h-1):
        for x in range(1, w-1):
            ans = max(ans, score(y,x))
    return ans


data = r'''
30373
25512
65332
33549
35390
'''
assert part1(data) == 21
assert part2(data) == 8


data = open('day8.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
