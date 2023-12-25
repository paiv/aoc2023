#!/usr/bin/env python
import math
import re
import sys


def part1(data):
    def wrap(line):
        xs = list(map(int, re.findall(r'-?\d+', line)))
        r = 0
        for x,y in zip(xs[::2], xs[1::2]):
            r = max(r, math.sqrt(x*x+y*y))
        return r
    data = data.strip().splitlines()
    ans = sum(map(wrap, data))
    return int(ans)


def part2(data):
    def circle(ps, rs):
        if not ps or len(rs) == 3:
            match len(rs):
                case 0:
                    return None
                case 1:
                    q, = rs
                    return (q, 0)
                case 2:
                    a,b = rs
                    q = (a+b)/2
                    r = abs(a-q)
                    return (q, r)
                case 3:
                    a,b,c = rs
                    u,v = b-a, c-a
                    ux,uy,vx,vy = u.real,u.imag, v.real,v.imag
                    d = 2 * (ux*vy - uy*vx)
                    x = (vy * (ux*ux + uy*uy) - uy * (vx*vx + vy*vy)) / d
                    y = (ux * (vx*vx + vy*vy) - vx * (ux*ux + uy*uy)) / d
                    q = x + y*1j
                    r = abs(q)
                    return (q+a, r)
        p = ps.pop()
        if (qr := circle(set(ps), rs)):
            q,r = qr
            if abs(q-p) <= r:
                return qr
        return circle(set(ps), rs | {p})
    
    def wrap(line):
        xs = list(map(int, re.findall(r'-?\d+', line)))
        ps = set((x+y*1j) for x,y in zip(xs[::2], xs[1::2]))
        c,r = circle(ps, set())
        return r
    data = data.strip().splitlines()
    ans = sum(map(wrap, data))
    return int(ans)


data = '''
(0, 4), (3, -2), (-1, -2), (-2, 0)
'''
assert part1(data) == 4

data = '''
(0, 4), (3, -2), (-1, -2), (-2, 0)
(-1, 0), (1, 4), (1, -4)
'''
assert part2(data) == 7


data = (open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin).read()
print('part1:', part1(data))
print('part2:', part2(data))
