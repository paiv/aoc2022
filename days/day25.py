#!/usr/bin/env python


def part1(data):
    ans = 0
    for s in data.strip().splitlines():
        ans += decode(s)
    ans = encode(ans)
    return ans


def decode(s):
    return sum( (5**i) * ('=-012'.index(c)-2)
        for i,c in enumerate(reversed(s)))


def encode(n):
    ps = list()
    r = 0
    while n:
        n, t = divmod(n, 5)
        t += r
        r = t > 2
        ps.append('012=-'[t%5])
    if r:
        ps.append('012=-'[r])
    return ''.join(reversed(ps))


assert         1 ==              decode('1')
assert         2 ==              decode('2')
assert         3 ==             decode('1=')
assert         4 ==             decode('1-')
assert         5 ==             decode('10')
assert         6 ==             decode('11')
assert         7 ==             decode('12')
assert         8 ==             decode('2=')
assert         9 ==             decode('2-')
assert        10 ==             decode('20')
assert        15 ==            decode('1=0')
assert        20 ==            decode('1-0')
assert      2022 ==         decode('1=11-2')
assert     12345 ==        decode('1-0---0')
assert 314159265 ==  decode('1121-1110-1=0')


assert         encode(1) ==              '1'
assert         encode(2) ==              '2'
assert         encode(3) ==             '1='
assert         encode(4) ==             '1-'
assert         encode(5) ==             '10'
assert         encode(6) ==             '11'
assert         encode(7) ==             '12'
assert         encode(8) ==             '2='
assert         encode(9) ==             '2-'
assert        encode(10) ==             '20'
assert        encode(15) ==            '1=0'
assert        encode(20) ==            '1-0'
assert      encode(2022) ==         '1=11-2'
assert     encode(12345) ==        '1-0---0'
assert encode(314159265) ==  '1121-1110-1=0'


data = r'''
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
'''
assert part1(data) == '2=-1=0'


data = open('day25.in').read()
print('part1:', part1(data))
