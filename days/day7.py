#!/usr/bin/env python
import itertools
import re
from collections import defaultdict


def walk(data):
    dirs = defaultdict(int)
    cwd = list()
    for bl in re.findall(r'^[$]([^$]*)', data, re.M):
        cmd,*res = bl.strip().splitlines()
        cmd,*args = cmd.split()
        if cmd == 'cd':
            fn, = args
            if fn == '/':
                cwd = []
            elif fn == '..':
                if cwd:
                    cwd.pop()
            else:
                cwd.append(fn)
        elif cmd == 'ls':
            m = sum(map(int, re.findall(r'\d+', '\n'.join(res))))
            ps = ['/'] + cwd
            while ps:
                dirs['/'.join(ps)] += m
                ps.pop()
    return dirs


def walk(data):
    dirs = defaultdict(int)
    for line in data.strip().splitlines():
        match line.split():
            case '$', 'cd', '/': cwd = ['/']
            case '$', 'cd', '..': cwd.pop()
            case '$', 'cd', d: cwd.append(d)
            case '$', 'ls': pass
            case 'dir', _: pass
            case x, _:
                for d in itertools.accumulate(cwd):
                    dirs[d] += int(x)
    return dirs


def part1(data):
    dirs = walk(data)
    ans = sum(n for n in dirs.values() if n <= 100000)
    return ans


def part2(data):
    dirs = walk(data)
    need = 30000000 - (70000000 - dirs['/'])
    ans = min(n for n in dirs.values() if n >= need)
    return ans


data = r'''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
assert part1(data) == 95437
assert part2(data) == 24933642


data = open('day7.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
