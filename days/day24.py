#!/usr/bin/env python
import itertools
import re


def part1(data, M=200000000000000, N=400000000000000):
    def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
    rt = range(M, N+1)
    def collides(a, b):
        u1, v1 = a[3], a[4]
        u2, v2 = b[3], b[4]
        d = u1 * v2 - u2 * v1
        if not d:
            return 0
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        c1 = x1 * (y1+v1) - y1 * (x1+u1)
        c2 = x2 * (y2+v2) - y2 * (x2+u2)
        x = (u1 * c2 - u2 * c1) / d
        y = (v1 * c2 - v2 * c1) / d
        if rt.start <= x < rt.stop and rt.start <= y < rt.stop:
            if sign(x-x1) == sign(u1) and sign(x-x2) == sign(u2):
                return 1
        return 0
    ps = list(map(int, re.findall(r'\-?\d+', data)))
    ps = [ps[i:i+6] for i in range(0, len(ps), 6)]
    ans = sum(collides(a,b) for a,b in itertools.combinations(ps, 2))
    return ans


def part2(data):
    import z3
    ps = list(map(int, re.findall(r'\-?\d+', data)))
    ps = [ps[i:i+6] for i in range(0, len(ps), 6)]
    x,y,z,u,v,w = z3.Ints('x y z u v w')
    s = z3.Solver()
    for i,(a,b,c,d,e,f) in enumerate(ps):
        t = z3.Int(f't{i}')
        s.add(t >= 0)
        s.add(x + t * u == a + t * d)
        s.add(y + t * v == b + t * e)
        s.add(z + t * w == c + t * f)
        if i > 2: break
    if s.check() == z3.sat:
        m = s.model()
        ans = m.evaluate(x + y + z)
        return ans


data = '''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''
assert part1(data, 7, 27) == 2
assert part2(data) == 47


data = open('day24.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
