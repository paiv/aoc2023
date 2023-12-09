#!/usr/bin/env python


def part1(data):
    def diffs(xs):
        if not any(xs): return 0
        ys = [b-a for a,b in zip(xs,xs[1:])]
        return ys[-1] + diffs(ys)
    def solve(line):
        xs = list(map(int, line.split()))
        return xs[-1] + diffs(xs)
    ans = sum(map(solve, data.strip().splitlines()))
    return ans


def part2(data):
    def diffs(xs):
        if not any(xs): return 0
        ys = [b-a for a,b in zip(xs,xs[1:])]
        return ys[0] - diffs(ys)
    def solve(line):
        xs = list(map(int, line.split()))
        return xs[0] - diffs(xs)
    ans = sum(map(solve, data.strip().splitlines()))
    return ans


data = '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''
assert part1(data) == 114
assert part2(data) == 2


data = open('day9.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
