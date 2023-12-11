#!/usr/bin/env python
from functools import partial
from itertools import combinations


def L1(r):
    return abs(r.real) + abs(r.imag)


def part2(data, T=1000000):
    gala = [(x+1j*y) for y,s in enumerate(data.strip().splitlines())
        for x,c in enumerate(s) if c == '#']
    xs,ys = [int(p.real) for p in gala], [int(p.imag) for p in gala]
    expax = list()
    ox,dx = 0, T-1
    for x in range(max(xs)+1):
        if x in xs:
            expax.extend(q+ox for q in gala if q.real == x)
        else:
            ox += dx
    expa = list()
    oy,dy = 0j, 1j*dx
    for y in range(max(ys)+1):
        if y in ys:
            expa.extend(q+oy for q in expax if q.imag == y)
        else:
            oy += dy
    ans = sum(L1(a-b) for a,b in combinations(expa, 2))
    return int(ans)


part1 = partial(part2, T=2)


data = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
assert part1(data) == 374
assert part2(data, T=10) == 1030
assert part2(data, T=100) == 8410


data = open('day11.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
