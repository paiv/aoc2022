#!/usr/bin/env python
import re
from collections import deque


class Node:
    def __init__(self, v):
        self.v = v
    def __repr__(self):
        return f'{self.v}'


def decrypt(data, K, T):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    xs = deque([Node(x * K) for x in ints(data)])
    M = len(xs)
    order = list(xs)
    for wave in range(T):
        for p in order:
            xs.rotate(-xs.index(p))
            p = xs.popleft()
            xs.rotate(-p.v % (M-1))
            xs.appendleft(p)
    z = next(i for i,p in enumerate(xs) if p.v == 0)
    xs.rotate(-z)
    ans = 0
    for _ in range(3):
        xs.rotate(-1000 % M)
        ans += xs[0].v
    return ans


def part1(data): return decrypt(data, K=1, T=1)
def part2(data): return decrypt(data, K=811589153, T=10)


data = r'''
1
2
-3
3
-2
0
4
'''
assert part1(data) == 3
assert part2(data) == 1623178306


data = open('day20.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
