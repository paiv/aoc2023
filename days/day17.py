#!/usr/bin/env python
import heapq
from functools import partial


def solve(data, A, B):
    data = data.strip().splitlines()
    w,h = len(data[0]), len(data)
    grid = {(y,x):int(c) for y,s in enumerate(data)
        for x,c in enumerate(s)}
    moves = ((1,0), (0,1), (0,-1), (-1,0))
    fringe = [(0,0,0,0,0)]
    seen = dict()
    goal = (h-1, w-1)
    inf = float('inf')
    while fringe:
        wei, py,px, ry,rx = heapq.heappop(fringe)
        if (py,px) == goal:
            return wei
        k = (py,px,ry,rx)
        if seen.get(k,inf) <= wei:
            continue
        seen[k] = wei
        for dy,dx in moves:
            if (dy,dx) == (ry,rx) or (dy,dx) == (-ry,-rx):
                continue
            dw = 0
            for s in range(1, B+1):
                p = (py+dy*s, px+dx*s)
                if (w := grid.get(p)) is not None:
                    dw += w
                    if s >= A:
                        heapq.heappush(fringe, (wei+dw, *p, dy,dx))


part1 = partial(solve, A=1, B=3)
part2 = partial(solve, A=4, B=10)


data = '''
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''
assert part1(data) == 102
assert part2(data) == 94


data = open('day17.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
