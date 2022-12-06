#!/usr/bin/env python


def part1(data, N=4):
    data = data.strip()
    for i in range(N, len(data)+2):
        if len(set(data[i-N:i])) == N:
            return i


def part2(data, N=14):
    data = data.strip()
    for i in range(N, len(data)+2):
        if len(set(data[i-N:i])) == N:
            return i


assert part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert part1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert part1('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
assert part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert part2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert part2('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26


data = open('day6.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
