#!/usr/bin/env python


def part1(data):
    lines = data.strip().splitlines()
    def rval(x):
        if isinstance(x, int):
            return x
        op,a,b = prog[x]
        return op(a, b)
    def op_add(a, b): return rval(a) + rval(b)
    def op_mul(a, b): return rval(a) * rval(b)
    def op_sub(a, b): return rval(a) - rval(b)
    def op_div(a, b): return rval(a) // rval(b)
    def op_val(a, _): return rval(a)

    prog = dict()
    for line in lines:
        s, op = line.strip().split(':')
        match op.split():
            case a,'+',b: prog[s] = [op_add, a,b]
            case a,'*',b: prog[s] = [op_mul, a,b]
            case a,'-',b: prog[s] = [op_sub, a,b]
            case a,'/',b: prog[s] = [op_div, a,b]
            case a,:
                if a.isdigit():
                    prog[s] = [op_val, int(a), None]
                else:
                    raise Exception(repr(line))
    ans = rval('root')
    return ans


def part2(data):
    lines = data.strip().splitlines()
    def rval(x):
        if isinstance(x, int):
            return x
        op,a,b = prog[x]
        return op(a, b)
    def op_add(a, b): return rval(a) + rval(b)
    def op_mul(a, b): return rval(a) * rval(b)
    def op_sub(a, b): return rval(a) - rval(b)
    def op_div(a, b): return rval(a) // rval(b)
    def op_val(a, _): return rval(a)

    prog = dict()
    for line in lines:
        s, op = line.strip().split(':')
        if s == 'root':
            a,_,b = op.split()
            prog[s] = [op_sub, a,b]
            continue
        match op.split():
            case a,'+',b: prog[s] = [op_add, a,b]
            case a,'*',b: prog[s] = [op_mul, a,b]
            case a,'-',b: prog[s] = [op_sub, a,b]
            case a,'/',b: prog[s] = [op_div, a,b]
            case a,:
                if a.isdigit():
                    prog[s] = [op_val, int(a), None]
                else:
                    raise Exception(repr(line))

    def sign(x): return 1 if x > 0 else -1 if x < 0 else 0

    def f(q):
        prog['humn'] = [op_val, q, None]
        return sign(rval('root'))

    l,r = 0,1
    while f(l) == f(r):
        r = r * 2
    while l != r - 1:
        m = (l + r) // 2
        if f(l) == f(m):
            l = m
        else:
            r = m
    ans = r
    return ans



data = r'''
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''
assert part1(data) == 152
assert part2(data) == 301


data = open('day21.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
