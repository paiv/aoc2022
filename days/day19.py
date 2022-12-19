#!/usr/bin/env python
import math
import re


def findmax(łs, T):
    łoo, łco, łso, łsc, łgo, łgs = łs
    maxo, maxc, maxs = max(łoo, łco, łso, łgo), łsc, łgs
    opt = {i:i*(i-1)//2 for i in range(1,T+1)}
    fringe = list()
    for r in range(4):
        fringe.append((0, r, 1, 0, 0, 0, 0, 0, 0, 0))
    ans = 0
    while fringe:
        t, rr, jo, jc, js, jg, no, nc, ns, ng = fringe.pop()
        if t == T:
            ans = max(ans, ng)
            continue
        if ng + (T-t)*jg + opt[T-t] < ans:
            continue
        if rr == 0 and jo < maxo and no >= łoo:
            for r in range(4):
                fringe.append((t+1, r, jo+1, jc, js, jg, no+jo-łoo, nc+jc, ns+js, ng+jg))
        elif rr == 1 and jc < maxc and no >= łco:
            for r in range(4):
                fringe.append((t+1, r, jo, jc+1, js, jg, no+jo-łco, nc+jc, ns+js, ng+jg))
        elif rr == 2 and js < maxs and no >= łso and nc >= łsc:
            for r in range(4):
                fringe.append((t+1, r, jo, jc, js+1, jg, no+jo-łso, nc+jc-łsc, ns+js, ng+jg))
        elif rr == 3 and no >= łgo and ns >= łgs:
            for r in range(4):
                fringe.append((t+1, r, jo, jc, js, jg+1, no+jo-łgo, nc+jc, ns+js-łgs, ng+jg))
        else:
            fringe.append((t+1, rr, jo, jc, js, jg, no+jo, nc+jc, ns+js, ng+jg))
    return ans


def part1(data, T=24):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    xs = [ints(s) for s in data.strip().splitlines()]
    ans = sum(pid * findmax(ps, T) for pid,*ps in xs)
    return ans


def part2(data, T=32):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    xs = [ints(s) for s in data.strip().splitlines()]
    ans = math.prod(findmax(ps, T) for pid,*ps in xs[:3])
    return ans


data = r'''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
'''
# assert part1(data) == 33
# assert part2(data) == 56*62


data = open('day19.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
