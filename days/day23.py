#!/usr/bin/env python
from collections import deque
from functools import cache


def part1(data):
    data = data.strip().splitlines()
    paths = {(x+y*1j):c for y,s in enumerate(data) for x,c in enumerate(s) if c != '#'}
    pois = {p for p in paths if sum((p+s in paths) for s in (1,-1,1j,-1j)) > 2}
    w,h = len(data[0]), len(data)
    slopes = dict(zip('><v^', [1,-1,1j,-1j]))
    start = 1+0j
    goal = (w-2)+(h-1)*1j
    pois.add(goal)

    @cache
    def find_paths(pos, pr):
        res = list()
        fringe = deque([(0,pos,pr)])
        seen = set()
        while fringe:
            d,p,pr = fringe.popleft()
            if p in pois and p != pos:
                res.append((d,p,pr))
                continue
            if p in seen: continue
            seen.add(p)
            for s in (1,-1,1j,-1j):
                q = p + s
                if q != pr and (c := paths.get(q)):
                    match c:
                        case '.':
                            fringe.append((d+1, q, p))
                        case _:
                            z,q = q, q+slopes[c]
                            if q in paths and q != p:
                                fringe.append((d+2, q, z))
        return res
    ans = 0
    fringe = [(0,start,0, [start])]
    seen = dict()
    while fringe:
        d,p,pr,ps = fringe.pop()
        if p == goal:
            ans = max(ans, d)
            # print(d)
            # display(data, ps)
            continue
        for s,q,qr in find_paths(p,pr):
            fringe.append((d+s, q, qr, ps+[q]))
    return ans


def display(board, path):
    so = ''
    for y,s in enumerate(board):
        for x,c in enumerate(s):
            p = x+y*1j
            m = '@' if p in path else c
            so += m
        so += '\n'
    print(so)


def part2(data):
    data = data.strip().splitlines()
    paths = {(x+y*1j):c for y,s in enumerate(data) for x,c in enumerate(s) if c != '#'}
    pois = {p for p in paths if sum((p+s in paths) for s in (1,-1,1j,-1j)) > 2}
    w,h = len(data[0]), len(data)
    slopes = dict(zip('><v^', [1,-1,1j,-1j]))
    start = 1+0j
    goal = (w-2)+(h-1)*1j
    pois.add(goal)

    @cache
    def find_paths(pos, pr):
        res = list()
        fringe = deque([(0,pos,pr)])
        seen = set()
        while fringe:
            d,p,pr = fringe.popleft()
            if p in pois and p != pos:
                res.append((d,p,pr))
                continue
            if p in seen: continue
            seen.add(p)
            for s in (1,-1,1j,-1j):
                q = p + s
                if q != pr and (c := paths.get(q)):
                    fringe.append((d+1, q, p))
        return res
    ans = 0
    fringe = [(0,start,0, {start})]
    while fringe:
        d,p,pr,ps = fringe.pop()
        if p == goal:
            ans = max(ans, d)
            continue
        for s,q,qr in find_paths(p,pr):
            if q not in ps:
                fringe.append((d+s, q, qr, ps|{q}))
    return ans


data = '''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''
assert part1(data) == 94
assert part2(data) == 154


data = open('day23.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
