#!/usr/bin/env python
import re


def part1(data):
    avail = dict(zip('rgb', [12, 13, 14]))
    def game(s):
        id,*draws = re.findall(r'\d+:|\d+ [rgb]', s)
        for q in draws:
            n,c = q.split()
            if int(n) > avail[c]:
                return 0
        return int(id[:-1])
    ans = sum(map(game, data.strip().splitlines()))
    return ans


def part2(data):
    def game(s):
        id,*draws = re.findall(r'\d+:|\d+ [rgb]', s)
        cubes = dict(zip('rgb', [0,0,0]))
        for q in draws:
            n,c = q.split()
            cubes[c] = max(int(n), cubes[c])
        return cubes['r'] * cubes['g'] * cubes['b']
    ans = sum(map(game, data.strip().splitlines()))
    return ans


data = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
assert part1(data) == 8
assert part2(data) == 2286


data = open('day2.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
