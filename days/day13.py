#!/usr/bin/env python


def part1(data):
    def refl(block):
        rows = block.split()
        for y in range(1, len(rows)):
            if all(a == b for a,b in zip(rows[:y][::-1], rows[y:])):
                return 100 * y
        cols = list(zip(*rows))
        for x in range(1, len(cols)):
            if all(a == b for a,b in zip(cols[:x][::-1], cols[x:])):
                return x
    ans = sum(map(refl, data.strip().split('\n\n')))
    return ans


def part2(data):
    def dist(p):
        return sum(x != y for x,y in zip(*p))
    def refl(block):
        rows = block.split()
        for y in range(1, len(rows)):
            if sum(map(dist, zip(rows[:y][::-1], rows[y:]))) == 1:
                return 100 * y
        cols = list(zip(*rows))
        for x in range(1, len(cols)):
            if sum(map(dist, zip(cols[:x][::-1], cols[x:]))) == 1:
                return x
    ans = sum(map(refl, data.strip().split('\n\n')))
    return ans


data = '''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''
assert part1(data) == 405
assert part2(data) == 400


data = open('day13.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
