#!/usr/bin/env python


def part1(data):
    board = list(map(list, data.strip().splitlines()))
    h = len(board)
    done = False
    while not done:
        done = True
        for y,row in enumerate(board):
            for x,c in enumerate(row):
                if y > 0 and c == 'O' and board[y-1][x] == '.':
                    board[y-1][x] = 'O'
                    board[y][x] = '.'
                    done = False
    ans = sum(row.count('O')*(h-y) for y,row in enumerate(board))
    return ans


def part2(data, N=1000000000):
    board = list(map(list, data.strip().splitlines()))
    w,h = len(board[0]), len(board)
    def cycle():
        done = False
        while not done:
            done = True
            for y,row in enumerate(board):
                for x,c in enumerate(row):
                    if y > 0 and c == 'O' and board[y-1][x] == '.':
                        board[y-1][x] = 'O'
                        board[y][x] = '.'
                        done = False
        done = False
        while not done:
            done = True
            for x,col in enumerate(zip(*board)):
                for y,c in enumerate(col):
                    if x > 0 and c == 'O' and board[y][x-1] == '.':
                        board[y][x-1] = 'O'
                        board[y][x] = '.'
                        done = False
        done = False
        while not done:
            done = True
            for y,row in enumerate(board):
                for x,c in enumerate(row):
                    if y+1 < h and c == 'O' and board[y+1][x] == '.':
                        board[y+1][x] = 'O'
                        board[y][x] = '.'
                        done = False
        done = False
        while not done:
            done = True
            for x,col in enumerate(zip(*board)):
                for y,c in enumerate(col):
                    if x+1 < w and c == 'O' and board[y][x+1] == '.':
                        board[y][x+1] = 'O'
                        board[y][x] = '.'
                        done = False
    seen = dict()
    for t in range(N):
        k = tuple((x+1j*y) for y,row in enumerate(board)
            for x,c in enumerate(row) if c == 'O')
        if (t0 := seen.get(k)) is not None:
            P = t - t0
            break
        seen[k] = t
        cycle()
    for _ in range((N-t) % P):
        cycle()
    ans = sum(row.count('O')*(h-y) for y,row in enumerate(board))
    return ans


def display(board, fps=3):
    h = len(board)
    ans = sum(row.count('O')*(h-y) for y,row in enumerate(board))
    print('\n'.join(map(''.join, board)))
    print(ans)
    print()
    if fps:
        time.sleep(1/fps)


data = '''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''
assert part1(data) == 136
assert part2(data) == 64


data = open('day14.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
