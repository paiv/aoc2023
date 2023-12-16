#!/usr/bin/env python
import time


def part1(data):
    board = {(x+1j*y):c for y,s in enumerate(data.strip().splitlines())
        for x,c in enumerate(s)}
    e = set()
    fringe = [(0,1)]
    seen = set()
    while fringe:
        p,d = fringe.pop()
        while p in board:
            k = (p,d)
            if k in seen: break
            seen.add(k)
            e.add(p)
            match board[p]:
                case '.':
                    p += d
                case '|':
                    if d.imag:
                        p += d
                    else:
                        u,v = d*1j, d*-1j
                        fringe.append((p+u, u))
                        fringe.append((p+v, v))
                case '-':
                    if d.real:
                        p += d
                    else:
                        u,v = d*1j, d*-1j
                        fringe.append((p+u, u))
                        fringe.append((p+v, v))
                case '/':
                    d *= [1j,-1j][d.real != 0]
                    p += d
                case '\\':
                    d *= [1j,-1j][d.real == 0]
                    p += d
    ans = len(e)
    return ans


def part2(data):
    data = data.strip().splitlines()
    w,h = len(data[0]), len(data)
    board = {(x+1j*y):c for y,s in enumerate(data) for x,c in enumerate(s)}
    def beam(pos,dir):
        e = set()
        fringe = [(pos,dir)]
        seen = set()
        while fringe:
            p,d = fringe.pop()
            while p in board:
                k = (p,d)
                if k in seen: break
                seen.add(k)
                e.add(p)
                match board[p]:
                    case '.':
                        p += d
                    case '|':
                        if d.imag:
                            p += d
                        else:
                            u,v = d*1j, d*-1j
                            fringe.append((p+u, u))
                            fringe.append((p+v, v))
                    case '-':
                        if d.real:
                            p += d
                        else:
                            u,v = d*1j, d*-1j
                            fringe.append((p+u, u))
                            fringe.append((p+v, v))
                    case '/':
                        d *= [1j,-1j][d.real != 0]
                        p += d
                    case '\\':
                        d *= [1j,-1j][d.real == 0]
                        p += d
        return len(e)
    
    start = list()
    start.extend((x+1j*y, d) for x in range(w) for y,d in [(0, 1j), (h-1, -1j)])
    start.extend((x+1j*y, d) for y in range(h) for x,d in [(0, 1), (w-1, -1)])
    
    ans = max(beam(p,d) for p,d in start)
    return ans


def display(board, pos, dir, seen=None, fps=2):
    z = board[pos]
    ps,board = board,defaultdict(list)
    for p,c in ps.items():
        board[int(p.imag)].append((int(p.real),c))
    ps,board = board,list()
    for y in sorted(ps.keys()):
        board.append([c for x,c in sorted(ps[y])])
    if seen:
        for p in seen:
            board[int(p.imag)][int(p.real)] = '#'
    uv = dict(zip([1,-1,1j,-1j], '><v^'))
    board[int(pos.imag)][int(pos.real)] = uv[dir]
    so = '\n'.join(map(''.join, board))
    if seen:
        print(len(seen), pos, dir, repr(z), uv[dir])
    print(so, end='\n\n', flush=True)
    if fps:
        time.sleep(1/fps)

    
data = r'''
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''
assert part1(data) == 46
assert part2(data) == 51


data = open('day16.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
