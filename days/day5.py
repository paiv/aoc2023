#!/usr/bin/env python
import re
from itertools import batched


def part1(data):
    def nums(s):
        return map(int, re.findall(r'\d+', s))
    def pblock(s):
        return [list(nums(l)) for l in s.strip().splitlines()[1:]]

    parts = data.strip().split('\n\n')
    seeds = list(nums(parts[0]))
    maps = list(map(pblock, parts[1:]))
    ans = float('inf')
    for pos in seeds:
        for bl in maps:
            for d,s,n in bl:
                if pos in range(s,s+n):
                    pos += d - s
                    break
        ans = min(ans, pos)
    return ans


def part2(data):
    def nums(s):
        return map(int, re.findall(r'\d+', s))
    def pblock(s):
        xs = [list(nums(l)) for l in s.strip().splitlines()[1:]]
        xs = sorted(xs, key=lambda p: p[1])
        return xs

    parts = data.strip().split('\n\n')
    maps = list(map(pblock, parts[1:]))
    def walk(ps, pn, py):
        if py >= len(maps):
            return ps
        res = float('inf')
        for d,s,n in maps[py]:
            if s+n <= ps:
                pass
            elif s >= ps+pn:
                break
            elif s > ps:
                res = min(res, walk(ps, s-ps, py+1))
                qn = min(s+n, ps+pn) - s
                res = min(res, walk(d, qn, py+1))
                pn -= qn
                ps += qn 
            else:
                qn = min(s+n, ps+pn) - ps
                res = min(res, walk(ps+d-s, qn, py+1))
                pn -= qn
                ps += qn
            if not pn: break
        if pn:
            res = min(res, walk(ps, pn, py+1))
        return res
    ans = min(walk(s,n, 0) for s,n in batched(nums(parts[0]), 2))
    return ans


data = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
assert part1(data) == 35
assert part2(data) == 46


data = open('day5.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
