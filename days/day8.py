#!/usr/bin/env python
import itertools
import math
import re


def part1(data):
    prog,nodes = data.strip().split('\n\n')
    nodes = {a:(b,c) for s in nodes.splitlines() for a,b,c in [re.findall(r'\w+',s)]}
    pos = 'AAA'
    goal = 'ZZZ'
    ans = 0
    for op in itertools.cycle(prog):
        if pos == goal: break
        pos = nodes[pos][op != 'L']
        ans += 1
    return ans


def part2(data):
    prog,nodes = data.strip().split('\n\n')
    nodes = {a:(b,c) for s in nodes.splitlines() for a,b,c in [re.findall(r'\w+',s)]}
    def runner(k):
        for op in itertools.cycle(prog):
            yield k
            k = nodes[k][op != 'L']
    def finish(r):
        t = 0
        for k in r:
            if k[-1] == 'Z':
                return t
            t += 1
    pos = [k for k in nodes if k[-1] == 'A']
    ms = [finish(runner(k)) for k in pos]
    ans = math.lcm(*ms)
    return ans


data = '''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''
assert part1(data) == 2

data = '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''
assert part1(data) == 6

data = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
assert part2(data) == 6


data = open('day8.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
