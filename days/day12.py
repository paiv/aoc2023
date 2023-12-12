#!/usr/bin/env python
from functools import cache, partial


def part2(data, N=5):
    @cache
    def arrs(s, e, x, xs):
        if not s:
            return 1 if (x == 0 and not xs) else 0
        match s[0]:
            case '.':
                if x: return 0
                return arrs(s[1:], 0, x, xs)
            case '#':
                if e: return 0
                if x == 0:
                    if not xs: return 0
                    x,xs = xs[0], xs[1:]
                return arrs(s[1:], x == 1, x-1, xs)
            case '?':
                if x:
                    return arrs(s[1:], x == 1, x-1, xs)
                else:
                    res = arrs(s[1:], 0, x, xs)
                    if not e and xs:
                        x,xs = xs[0], xs[1:]
                        res += arrs(s[1:], x == 1, x-1, xs)
                    return res
    def precord(line):
        mask,xs = line.split()
        xs = tuple(map(int, xs.split(',')))
        mask = '?'.join([mask] * N)
        xs *= N
        return arrs(mask, 0, 0, xs)
    ans = sum(map(precord, data.strip().splitlines()))
    return ans


part1 = partial(part2, N=1)


data = '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
assert part1(data) == 21
assert part2(data) == 525152


data = open('day12.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
