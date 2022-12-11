#!/usr/bin/env python
import math
import re
from collections import deque


def parse(data):
    blocks = data.strip().split('\n\n')
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))

    def parse_op(op):
        match op.split():
            case 'old', '+', 'old':
                return lambda x: x + x
            case 'old', '+', r:
                r = int(r)
                return lambda x: x + r
            case 'old', '*', 'old':
                return lambda x: x * x
            case 'old', '*', r:
                r = int(r)
                return lambda x: x * r
            case _: raise Exception(repr(op))

    monkeys = list()
    for bl in blocks:
        ms = bl.strip().splitlines()
        mid, = ints(ms[0])
        items = ints(ms[1])
        _,op = re.split(r' new =\s*', ms[2])
        test, = ints(ms[3])
        ft, = ints(ms[4])
        ff, = ints(ms[5])
        monkeys.append([mid, deque(items), parse_op(op), test, ft, ff])
    return monkeys


def part1(data, N=20):
    monkeys = parse(data)
    stats = [0] * len(monkeys)
    for _ in range(N):
        for mid, items, op, test, ft, ff in monkeys:
            for n in items:
                stats[mid] += 1
                n = op(n) // 3
                if n % test:
                    monkeys[ff][1].append(n)
                else:
                    monkeys[ft][1].append(n)
            items.clear()
    x,y = sorted(stats)[-2:]
    ans = x * y
    return ans


def part2(data, N=10000):
    monkeys = parse(data)
    M = math.prod(m[3] for m in monkeys)
    stats = [0] * len(monkeys)
    for _ in range(N):
        for mid, items, op, test, ft, ff in monkeys:
            for n in items:
                stats[mid] += 1
                n = op(n) % M
                if n % test:
                    monkeys[ff][1].append(n)
                else:
                    monkeys[ft][1].append(n)
            items.clear()
    x,y = sorted(stats)[-2:]
    ans = x * y
    return ans


data = r'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
assert part1(data) == 10605
assert part2(data) == 2713310158


data = open('day11.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
