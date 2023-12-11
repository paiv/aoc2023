#!/usr/bin/env python


def part1(data):
    board = {(x+1j*y):c for y,s in enumerate(data.strip().splitlines())
        for x,c in enumerate(s)}
    S = next(k for k,c in board.items() if c == 'S')
    conn = {
        '|':[-1j,1j],
        '-':[-1,1],
        'L':[-1j,1],
        'J':[-1j,-1],
        '7':[1j,-1],
        'F':[1j,1],
    }
    pos = S
    for s in [1,-1,1j,-1j]:
        if (c := board.get(pos+s)) and (-s in conn[c]):
            out = s
            break
    ans = 0
    while True:
        ans += 1
        pos += out
        if pos == S: break
        cs = conn[board[pos]]
        out = cs[1-cs.index(-out)]
    return ans // 2


def part2(data):
    board = {(x+1j*y):c for y,s in enumerate(data.strip().splitlines())
        for x,c in enumerate(s)}
    S = next(k for k,c in board.items() if c == 'S')
    conn = {
        '|':[-1j,1j],
        '-':[-1,1],
        'L':[-1j,1],
        'J':[-1j,-1],
        '7':[1j,-1],
        'F':[1j,1],
    }
    pos = S
    for s in [1,-1,1j,-1j]:
        if (c := board.get(pos+s)) and (-s in conn[c]):
            out = s
            break
    ans = 0
    dist = 0
    while True:
        dist += 1
        ans += out.real * pos.imag
        pos += out
        if pos == S: break
        cs = conn[board[pos]]
        out = cs[1-cs.index(-out)]
    ans = abs(int(ans)) - dist // 2 + 1
    return ans


data = '''
.....
.S-7.
.|.|.
.L-J.
.....
'''
assert part1(data) == 4

data = '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''
assert part1(data) == 8

data = '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''
assert part2(data) == 4

data = '''
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
'''
assert part2(data) == 4

data = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''
assert part2(data) == 8

data = '''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''
assert part2(data) == 10


data = open('day10.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
