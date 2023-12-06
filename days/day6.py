#!/usr/bin/env python
import math


def part1(data):
    ts,ds = data.strip().splitlines()
    ts = list(map(int, ts.split()[1:]))
    ds = list(map(int, ds.split()[1:]))
    races = dict(zip(ts, ds))
    wins = [0] * len(races)
    for v in range(max(races)+1):
        for i, (t, d) in enumerate(races.items()):
            pos = v * (t - v)
            if pos > d:
                wins[i] += 1
    ans = 1
    for x in wins:
        ans *= x
    return ans


def part2(data):
    ts,ds = data.strip().splitlines()
    t = int(''.join(ts.split()[1:]))
    d = int(''.join(ds.split()[1:]))
    ans = 0
    for v in range(t+1):
        pos = v * (t - v)
        if pos > d:
            ans += 1
    return ans


def part2(data):
    ts,ds = data.strip().splitlines()
    t = int(''.join(ts.split()[1:]))
    d = int(''.join(ds.split()[1:]))
    x = round((t - math.sqrt(t*t - 4*d)) / 2 + 0.5)
    ans = t - 2*x + 1
    return ans


data = '''
Time:      7  15   30
Distance:  9  40  200
'''
assert part1(data) == 288
assert part2(data) == 71503


data = open('day6.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
