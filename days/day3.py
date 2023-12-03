#!/usr/bin/env python


def part1(data):
    data = data.strip().splitlines()
    nums = list()
    pois = dict()
    for y,s in enumerate(data):
        n = None
        for x,c in enumerate(s):
            p = x + 1j * y
            if c.isdigit():
                if n is None:
                    n = [y, x, x+1]
                else:
                    n[-1] = x+1
            else:
                if n:
                    nums.append(tuple(n))
                    n = None
                if c != '.':
                    pois[p] = c
        if n:
            nums.append(tuple(n))

    adj = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
    ans = 0
    for y, x, z in nums:
        if any((q+s+1j*y) in pois for q in range(x,z) for s in adj):
            ans += int(data[y][x:z])
    return ans


def part2(data):
    data = data.strip().splitlines()
    board = {(x+1j*y):c for y,s in enumerate(data) for x,c in enumerate(s) if c != '.'}
    adj = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
    nums = list()
    pois = dict()
    for y,s in enumerate(data):
        nums.append(list())
        n = None
        for x,c in enumerate(s):
            p = x + 1j * y
            if c.isdigit():
                if n is None:
                    n = [y, x, x+1]
                else:
                    n[-1] = x+1
            else:
                if n:
                    nums[y].append(tuple(n))
                    n = None
                if c == '*':
                    if any(board.get(p+j, '').isdigit() for j in adj):
                        pois[p] = c
        if n:
            nums[y].append(tuple(n))

    def find(pos):
        r = int(pos.imag)
        res = 1
        t = 0
        for y in range(r-1, r+2):
            for _, x, z in nums[y]:
                if any((p+s) == pos for q in range(x,z) for p in [q+1j*y] for s in adj):
                    res *= int(data[y][x:z])
                    t += 1
        return t, res
    
    ans = 0
    for p in pois:
        n,v = find(p)
        if n == 2:
            ans += v
    return ans 


data = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
assert part1(data) == 4361
assert part2(data) == 467835


data = open('day3.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
