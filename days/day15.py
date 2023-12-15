#!/usr/bin/env python
import re


def part1(data):
    def hash(s):
        h = 0
        for c in map(ord, s):
            h = (h + c) * 17 % 256
        return h
    ans = sum(map(hash, data.strip().split(',')))
    return ans


def part2(data):
    def hash(s):
        h = 0
        for c in map(ord, s):
            h = (h + c) * 17 % 256
        return h
    bins = [dict() for _ in range(256)]
    for s,op,n in re.findall(r'(\w+)([=-])(\d+)?', data):
        i = hash(s)
        match op:
            case '-':
                bins[i].pop(s, None)
            case '=':
                bins[i][s] = int(n)
    ans = sum(i*j*x for i,d in enumerate(bins,1)
        for j,x in enumerate(d.values(),1))
    return ans


data = '''
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''
assert part1(data) == 1320
assert part2(data) == 145


data = open('day15.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
