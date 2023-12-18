#!/usr/bin/env python


def part1(data):
    moves = dict(zip('RLDU', [1,-1,1j,-1j]))
    pos = 0
    dist = 0
    ans = 0
    for v,n,c in (s.split() for s in data.strip().splitlines()):
        n = int(n)
        v = moves[v]
        ans += pos.imag * v.real * n
        pos += v * n
        dist += n
    ans = abs(int(ans)) - dist // 2 + 1 + dist
    return ans


def part2(data):
    moves = dict(zip('0213', [1,-1,1j,-1j]))
    pos = 0
    dist = 0
    ans = 0
    for v,n,c in (s.split() for s in data.strip().splitlines()):
        n = int(c[2:7], 16)
        v = moves[c[7]]
        ans += pos.imag * v.real * n
        pos += v * n
        dist += n
    ans = abs(int(ans)) - dist // 2 + 1 + dist
    return ans


data = '''
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''
assert part1(data) == 62
assert part2(data) == 952408144115


data = open('day18.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
