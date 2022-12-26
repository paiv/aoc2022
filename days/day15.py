#!/usr/bin/env python
import itertools
import re


def part1(data, Y=2000000):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    lines = data.strip().splitlines()
    beacons = set()
    l,r = float('inf'), float('-inf')
    for line in lines:
        sx,sy,bx,by = ints(line)
        if by == Y:
            beacons.add(bx)
        d = abs(sx-bx) + abs(sy-by)
        if (t := abs(Y - sy)) < d:
            d -= t
            l = min(l, sx-d)
            r = max(r, sx+d)
    ans = r - l + 1 - len(beacons)
    return ans


def part2(data, W=4000000):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    lines = data.strip().splitlines()
    beacons = set()
    for line in lines:
        sx,sy,bx,by = ints(line)
        beacons.add((bx,by))
    seen = set()
    while True:
        Y = random.randrange(W+1)
        if Y in seen: continue
        seen.add(Y)
        chunks = [(0, W)]
        for line in lines:
            sx,sy,bx,by = ints(line)
            dist = abs(sx-bx) + abs(sy-by)
            if (n := abs(Y - sy)) < dist:
                w = dist - n
                l,r = sx-w, sx+w
                dawn = list()
                for a,b in chunks:
                    if (r < a) or (b < l):
                        dawn.append([a,b])
                    else:
                        if a < l: dawn.append([a, l-1])
                        if r < b: dawn.append([r+1, b])
                chunks = dawn
        if chunks:
            (a,b), = chunks
            assert a == b
            ans = a * 4000000 + Y
            print(ans)
            return ans


def part2(data, W=4000000):
    def ints(s): return list(map(int, re.findall(r'-?\d+', s)))
    def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
    lines = data.strip().splitlines()
    scanners = dict()
    beacons = set()
    asides = set()
    bsides = set()
    for line in lines:
        sx,sy,bx,by = ints(line)
        r = dist((sx,sy), (bx,by))
        scanners[(sx,sy)] = r
        beacons.add((bx,by))
        asides.add(sy-sx-r-1)
        asides.add(sy-sx+r+1)
        bsides.add(sy+sx+r+1)
        bsides.add(sy+sx-r-1)
    for a,b in itertools.product(asides, bsides):
        px,py = (b-a)//2, (b+a)//2
        if px in range(W) and py in range(W):
            if all(dist(s, (px,py)) > r for s,r in scanners.items()):
                ans = 4000000 * px + py
                print(ans)
                return ans


data = r'''
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
assert part1(data, Y=10) == 26
assert part2(data, W=20) == 56000011


data = open('day15.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
