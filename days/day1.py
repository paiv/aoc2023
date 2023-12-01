#!/usr/bin/env python
import re


def part1(data):
    def check(s):
        q = [c for c in s if c.isdigit()]
        return int(q[0] + q[-1])
    ans = sum(map(check, data.split()))
    return ans


def part2(data):
    digits = list('123456789')
    names = 'one two three four five six seven eight nine'.split()
    guide = dict(zip(digits+names, digits+digits))
    def check(s):
        q = sorted((s.index(k), n) for k,n in guide.items() if k in s)
        t = sorted((s.rindex(k), n) for k,n in guide.items() if k in s)
        res = int(q[0][1] + t[-1][1])
        return res
    ans = sum(map(check, data.split()))
    return ans


def part2(data):
    digits = list('123456789')
    names = 'one two three four five six seven eight nine'.split()
    guide = dict(zip(digits+names, digits+digits))
    ks = '|'.join(guide.keys())
    rx = re.compile(f'(?=({ks}))')
    def check(s):
        xs = [guide[k] for k in rx.findall(s)]
        return int(xs[0] + xs[-1])
    ans = sum(map(check, data.split()))
    return ans


data = '''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
assert part1(data) == 142

data = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
assert part2(data) == 281


data = open('day1.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
