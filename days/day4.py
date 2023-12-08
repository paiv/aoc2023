#!/usr/bin/env python
import re


def part1(data):
    def score(line):
        a,b = line.split('|')
        _,*ws = map(int, re.findall(r'\d+', a))
        *ms, = map(int, re.findall(r'\d+', b))
        t = len(set(ws) & set(ms))
        res = 2 ** (t-1) if t else 0
        return res
    ans = sum(map(score, data.strip().splitlines()))
    return ans


def part2(data):
    def pcard(line):
        a,b = line.split('|')
        _,*ws = map(int, re.findall(r'\d+', a))
        *ms, = map(int, re.findall(r'\d+', b))
        return len(set(ws) & set(ms))
    cards = [pcard(s) for s in data.strip().splitlines()]
    ans = [1] * len(cards)
    for i,w in enumerate(cards):
        for j in range(i+1, i+1+w):
            ans[j] += ans[i]
    ans = sum(ans)
    return ans


data = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
assert part1(data) == 13
assert part2(data) == 30


data = open('day4.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
