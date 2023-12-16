#!/usr/bin/env python


def part1(data):
    cards = dict(zip('23456789TJQKA', [2,3,4,5,6,7,8,9,10,11,12,13,15]))
    def horder(hand):
        hs,bet = hand
        cs = tuple(cards[c] for c in hs)
        s = set(hs)
        if len(s) == 1:
            return (7, cs)
        if len(s) == 2:
            a,b = s
            if hs.count(a) in (1,4):
                return (6, cs)
            if hs.count(a) in (2,3):
                return (5, cs)
        if len(s) == 3:
            a,b,c = s
            na,nb,nc = hs.count(a), hs.count(b), hs.count(c)
            ns = sorted([na,nb,nc])
            if ns == [1,1,3]:
                return (4, cs)
            if ns == [1,2,2]:
                return (3, cs)
        if len(s) == 4:
            return (2, cs)
        return (1,cs)
        
    hands = [(p[0], int(p[1])) for s in data.strip().splitlines() for p in [s.split()]]
    hands = sorted(hands, key=horder)
    ans = sum((x*i) for i,(_,x) in enumerate(hands,1))
    return ans


def part2(data):
    cards = dict(zip('J23456789TQKA', [2,3,4,5,6,7,8,9,10,11,12,13,15]))
    def horder(hand):
        hs,bet = hand
        cs = tuple(cards[c] for c in hs)
        s = set(hs) - {'J'}
        j = hs.count('J')
        if j == 5:
            return (7, cs)
        elif j == 4:
            return (7, cs)
        elif j == 3:
            if len(s) == 1:
                return (7, cs)
            return (6, cs)
        elif j == 2:
            if len(s) == 1:
                return (7, cs)
            elif len(s) == 2:
                return (6, cs)
            return (4, cs)
        elif j == 1:
            if len(s) == 1:
                return (7, cs)
            elif len(s) == 2:
                a,b = s
                if hs.count(a) in (1,3):
                    return (6, cs)
                return (5, cs)
            elif len(s) == 3:
                return (4, cs)
            return (2, cs)
        else:
            if len(s) == 1:
                return (7, cs)
            if len(s) == 2:
                a,b = s
                if hs.count(a) in (1,4):
                    return (6, cs)
                if hs.count(a) in (2,3):
                    return (5, cs)
            if len(s) == 3:
                a,b,c = s
                na,nb,nc = hs.count(a), hs.count(b), hs.count(c)
                ns = sorted([na,nb,nc])
                if ns == [1,1,3]:
                    return (4, cs)
                if ns == [1,2,2]:
                    return (3, cs)
            if len(s) == 4:
                return (2, cs)
            return (1,cs)
        
    hands = [(p[0], int(p[1])) for s in data.strip().splitlines() for p in [s.split()]]
    hands = sorted(hands, key=horder)
    ans = sum((x*i) for i,(_,x) in enumerate(hands,1))
    return ans


data = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''
assert part1(data) == 6440
assert part2(data) == 5905


data = open('day7.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
