#!/usr/bin/env python
import itertools
import re
from collections import defaultdict
from functools import cache


def part1(data, T=30):
    neib = defaultdict(set)
    wei = dict()
    names = dict()
    ids = dict()
    for s,x,ds in re.findall(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w[\w, ]+)', data):
        for t in re.findall(r'\w+', ds):
            neib[s].add(t)
            neib[t].add(s)
        if (x := int(x)) or (s == 'AA'):
            i = len(wei)
            names[i] = s
            ids[s] = i
            wei[i] = x

    dist = pairwise_distance(neib, list(ids.keys()))
    N = len(names)
    mask = [1<<i for i in range(N)]

    AA = ids['AA']
    fringe = deque([(0, 0, 0, AA, mask[AA])])
    ans = 0
    while fringe:
        acc, t, cur, p, seen = fringe.popleft()
        ans = max(ans, (acc + cur * (T-t)))
        if t >= T: continue
        for s,m in enumerate(mask):
            if seen & m == 0:
                if (q := dist[p][s] + 1 + t) <= T:
                    w = wei[s]
                    fringe.append((acc+cur*(q-t), q, cur+w, s, seen|m))
                else:
                    fringe.append((acc+cur*(T-t), T, cur, s, seen))
    return ans


def pairwise_distance(neib, select):
    names = list(select) + list(set(neib.keys()) - set(select))
    N = len(names)
    inf = N * N
    dist = [[1 if j in neib[i] else 0 if i == j else inf for j in names] for i in names]
    for k,i,j in itertools.product(range(N), repeat=3):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    n = len(select)
    res = [[dist[i][j] for j in range(n)] for i in range(n)]
    return res


def part1(data, T=30):
    neib = defaultdict(set)
    wei = dict()
    names = dict()
    ids = dict()
    for s,x,ds in re.findall(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w[\w, ]+)', data):
        for t in re.findall(r'\w+', ds):
            neib[s].add(t)
            neib[t].add(s)
        if (x := int(x)) or (s == 'AA'):
            i = len(wei)
            names[i] = s
            ids[s] = i
            wei[i] = x

    dist = pairwise_distance(neib, list(ids.keys()))
    N = len(names)
    mask = [1<<i for i in range(N)]

    @cache
    def inner(t, seen, pos):
        if not t: return 0
        ans = 0
        for s,m in enumerate(mask):
            if seen & m == 0:
                d = min(t, dist[pos][s]+1)
                ans = max(ans, wei[s]*(t-d) + inner(t-d, seen|m, s))
        return ans

    start = ids['AA']
    ans = inner(T, mask[start], start)
    return ans


def part2(data, T=26):
    neib = defaultdict(set)
    wei = dict()
    names = dict()
    ids = dict()
    for s,x,ds in re.findall(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w[\w, ]+)', data):
        for t in re.findall(r'\w+', ds):
            neib[s].add(t)
            neib[t].add(s)
        if (x := int(x)) or (s == 'AA'):
            i = len(wei)
            names[i] = s
            ids[s] = i
            wei[i] = x

    dist = pairwise_distance(neib, list(ids.keys()))
    N = len(names)
    mask = [1<<i for i in range(N)]

    @cache
    def inner(t, seen, pos, flag):
        if not t: return 0
        ans = inner(T, seen, start, False) if flag else 0
        for s,m in enumerate(mask):
            if seen & m == 0:
                d = min(t, dist[pos][s]+1)
                ans = max(ans, wei[s] * (t-d) + inner(t-d, seen|m, s, flag))
        return ans

    start = ids['AA']
    ans = inner(T, mask[start], start, True)
    return ans


def part2(data, T=26):
    rx = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w[\w, ]+)')
    neib = {s:set(re.findall(r'\w+',ds)) for s,x,ds in rx.findall(data)}
    dist = {i:{j:1 if j in ps else 0 if i==j else float('inf') for j in neib} for i,ps in neib.items()}
    for k,i,j in itertools.product(dist, repeat=3):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    wei = {s:int(x) for s,x,ds in rx.findall(data) if int(x)}
    ids = {s:(1<<i) for i,s in enumerate(wei)}

    def inner(t, seen, pos, flow, acc):
        acc[seen] = max(flow, acc.get(seen,0))
        for s,m in ids.items():
            d = dist[pos][s] + 1
            if seen & m or d >= t: continue
            inner(t-d, seen|m, s, flow + (t-d) * wei[s], acc)
        return acc

    state = inner(T, 0, 'AA', 0, dict())
    ans = max(a+b for i,a in state.items() for j,b in state.items() if not i & j)
    return ans


data = r'''
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''
assert part1(data) == 1651
assert part2(data) == 1707


data = open('day16.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
