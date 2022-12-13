#!/usr/bin/env python


def compare(a, b):
    match isinstance(a, int), isinstance(b, int):
        case True, True: return sign(b - a)
        case False, True: return compare(a, [b])
        case True, False: return compare([a], b)
        case False, False:
            match len(a), len(b):
                case 0, 0: return 0
                case 0, _: return 1
                case _, 0: return -1
            if (r := compare(a[0], b[0])): return r
            return compare(a[1:], b[1:])


def sign(x): return 1 if x > 0 else -1 if x < 0 else 0


def bubble(a, compare):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if compare(a[i], a[j]) == -1:
                a[i], a[j] = a[j], a[i]


def part1(data):
    blocks = data.strip().split('\n\n')
    ans = 0
    for i,bl in enumerate(blocks):
        a,b = (eval(s) for s in bl.strip().splitlines())
        if compare(a, b) > 0:
            ans += i + 1
    return ans


def part2(data):
    data = data.replace('\n\n', '\n')
    lines = [[[2]], [[6]]] + [eval(s) for s in data.strip().splitlines()]
    a,b = lines[:2]
    bubble(lines, compare)
    i, j = lines.index(a), lines.index(b)
    ans = (i + 1) * (j + 1)
    return ans


data = r'''
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''
assert part1(data) == 13
assert part2(data) == 140


data = open('day13.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
