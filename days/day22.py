#!/usr/bin/env python


def part1(data):
    data = data.strip().splitlines()
    ww = [0,0,0]
    def pbr(s):
        a,b = s.split('~')
        xa,ya,za = map(int, a.split(','))
        xb,yb,zb = map(int, b.split(','))
        ww[0] = max(ww[0], zb)
        ww[1] = max(ww[1], yb)
        ww[2] = max(ww[2], xb)
        return [[z,y,x] for z in range(za,zb+1) for y in range(ya,yb+1) for x in range(xa,xb+1)]
    bricks = [pbr(s) for s in data]
    zw,yw,xw = (x+1 for x in ww)
    cubes = [[[None for _ in range(xw)] for _ in range(yw)] for _ in range(zw)]
    for bi,br in enumerate(bricks):
        for z,y,x in br:
            cubes[z][y][x] = bi
    def is_falling(i):
        ok = (i, None)
        for z,y,x in bricks[i]:
            if z <= 1: return False
            if cubes[z-1][y][x] not in ok:
                return False
        return True
    def fall1(i):
        ps = bricks[i]
        wipe(i)
        for p in ps:
            p[0] -= 1
        unwipe(i)
    def wipe(i):
        ps = bricks[i]
        for j,(z,y,x) in enumerate(ps):
            cubes[z][y][x] = None
    def unwipe(i):
        ps = bricks[i]
        for j,(z,y,x) in enumerate(ps):
            cubes[z][y][x] = i

    def is_stable():
        for z in range(2, zw):
            for y in range(yw):
                for x in range(xw):
                    if (bi := cubes[z][y][x]) is not None:
                        if is_falling(bi):
                            return False
        return True
        
    done = False
    while not done:
        done = True
        for z in range(2, zw):
            for y in range(yw):
                for x in range(xw):
                    if (bi := cubes[z][y][x]) is not None:
                        if is_falling(bi):
                            fall1(bi)
                            done = False
    ans = 0
    for i,br in enumerate(bricks):
        wipe(i)
        ans += is_stable()
        unwipe(i)
    return ans


def part2(data):
    data = data.strip().splitlines()
    ww = [0,0,0]
    def pbr(s):
        a,b = s.split('~')
        xa,ya,za = map(int, a.split(','))
        xb,yb,zb = map(int, b.split(','))
        ww[0] = max(ww[0], zb)
        ww[1] = max(ww[1], yb)
        ww[2] = max(ww[2], xb)
        return [[z,y,x] for z in range(za,zb+1) for y in range(ya,yb+1) for x in range(xa,xb+1)]
    bricks = [pbr(s) for s in data]
    zw,yw,xw = (x+1 for x in ww)
    cubes = [[[None for _ in range(xw)] for _ in range(yw)] for _ in range(zw)]
    for bi,br in enumerate(bricks):
        for z,y,x in br:
            cubes[z][y][x] = bi
    def is_falling(i):
        ok = (i, None)
        for z,y,x in bricks[i]:
            if z <= 1: return False
            if cubes[z-1][y][x] not in ok:
                return False
        return True
    def fall1(i):
        ps = bricks[i]
        wipe(i)
        for p in ps:
            p[0] -= 1
        unwipe(i)
    def wipe(i):
        ps = bricks[i]
        for j,(z,y,x) in enumerate(ps):
            cubes[z][y][x] = None
    def unwipe(i):
        ps = bricks[i]
        for j,(z,y,x) in enumerate(ps):
            cubes[z][y][x] = i
    def save_state():
        return [[list(p) for p in b] for b in bricks]
    def restore_state(s):
        for i,b in enumerate(bricks):
            wipe(i)
        for i,b in enumerate(s):
            bricks[i] = [list(x) for x in b]
            unwipe(i)

    def count_unstable():
        seen = set()
        for z in range(2, zw):
            for y in range(yw):
                for x in range(xw):
                    if (bi := cubes[z][y][x]) is not None:
                        if is_falling(bi):
                            seen.add(bi)
                            fall1(bi)
        return len(seen)
    
    done = False
    while not done:
        done = True
        for z in range(2, zw):
            for y in range(yw):
                for x in range(xw):
                    if (bi := cubes[z][y][x]) is not None:
                        if is_falling(bi):
                            fall1(bi)
                            done = False
    ans = 0
    s = save_state()
    for i,br in enumerate(bricks):
        wipe(i)
        ans += count_unstable()
        restore_state(s)
    return ans


data = '''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''
assert part1(data) == 5
assert part2(data) == 7


data = open('day22.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
