#!/usr/bin/env python
from collections import deque


def part1(data, N=64):
    data = data.strip().splitlines()
    S = None
    board = set()
    for y,s in enumerate(data):
        for x,c in enumerate(s):
            p = x+y*1j
            if c == 'S':
                S = p
                board.add(p)
            if c == '.':
                board.add(p)
    fringe = deque([(0,S)])
    seen = set()
    ans = 0
    while fringe:
        n,p = fringe.popleft()
        if p in seen: continue
        seen.add(p)
        if n % 2 == 0:
            ans += 1
        if n == N:
            continue
        for s in (1,-1,1j,-1j):
            q = p + s
            if q in board:
                fringe.append((n+1,q))
    return ans


def display(board, seen):
    so = ''
    for y,s in enumerate(board):
        so += ''.join('O' if p in seen else c for x,c in enumerate(s) for p in [(x+y*1j)]) + '\n'
    print(so)
    

def part2(data, N=26501365):
    data = data.strip().splitlines()
    w,h = len(data[0]),len(data)
    S = None
    for y,s in enumerate(data):
        for x,c in enumerate(s):
            if c == 'S':
                S = (y,x)
                break
    def sequence(data, N):
        ans = list()
        fringe = [S]
        seen = set()
        eo = [0,0]
        P = None
        for t in range(N+1):
            wave, fringe = fringe, list()
            while wave:
                p = wave.pop()
                if p in seen: continue
                seen.add(p)
                eo[t&1] += 1
                for sy,sx in [(0,1),(0,-1),(1,0),(-1,0)]:
                    y = p[0] + sy
                    x = p[1] + sx
                    c = data[y % h][x % w]
                    if c in '.S':
                        fringe.append((y,x))
            ans.append(eo[t&1])
            for i in range(1,len(ans)//2):
                x = ans[i::i]
                d = [b-a for a,b in zip(x,x[1:])]
                q = [b-a for a,b in zip(d,d[1:])]
                if len(q) > 2 and len(set(q)) == 1:
                    return (i,ans)
    P,xs = sequence(data, N)
    i = N%P
    x = xs[i::P]
    d = [b-a for a,b in zip(x,x[1:])]
    a = d[1] - d[0]
    b,c = d[0], x[1]
    def gen(a,b,c):
        def res(i): return ((i*i+i)//2 * a + i * b + c)
        return res
    res = gen(a,b,c)
    assert x[1:] == [res(i) for i in range(len(x)-1)]
    ans = res(N//P-1)
    return ans


data = '''
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''
assert part1(data, 6) == 16


data = open('day21.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
