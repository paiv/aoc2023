#!/usr/bin/env python
import math
from collections import defaultdict, deque


def part1(data, N=1000):
    par = defaultdict(set)
    chi = defaultdict(list)
    typ = dict()
    for line in data.strip().splitlines():
        n,ps = line.split('->')
        n = n.strip()
        if n not in ('broadcaster','output'):
            k,n = n[0],n[1:]
            typ[n] = k
        else:
            typ[n] = n[0]
        for p in ps.split(','):
            p = p.strip()
            par[p].add(n)
            chi[n].append(p)
    flops = {k:0 for k,t in typ.items() if t == '%'}
    cons = {k:{c:0 for c in par[k]} for k,t in typ.items() if t == '&'}

    stat = {0:0, 1:0}
    wire = deque()
    def send(d, s, v):
        # print('send', v, s, '->', d)
        wire.append((d,s,v))
    def recv(d, s, v):
        # print('recv', v, s, '->', d)
        stat[v] += 1
        match typ.get(d):
            case '%':
                o = flops[d]
                if not v:
                    v = 0 if o else 1
                    flops[d] = v
                    for c in chi[d]:
                        send(c, d, v)
            case '&':
                cons[d][s] = v
                v = 0 if all(cons[d].values()) else 1
                for c in chi[d]:
                    send(c, d, v)
            case _:
                for c in chi.get(d, list()):
                  send(c, d, v)
    def cycle():
        send('broadcaster', None, 0)
        while wire:
            ps = wire.popleft()
            recv(*ps)
        k = ','.join(f'{k}:{v}' for k,v in flops.items())
        return k

    seen = dict()
    k = ','.join(f'{k}:{v}' for k,v in flops.items())
    seen[k] = 0
    P,M = 0,1
    for t in range(1,N+1):
        k = cycle()
        if (t0 := seen.get(k)) is not None:
            P = t - t0
            break
        seen[k] = t
    if P:
        M = (N-t) // P + 1
        for t in range((N-t) % P):
            cycle()
    
    ans = stat[0] * stat[1] * M * M
    return ans


def part2(data, probe='rx'):
    par = defaultdict(set)
    chi = defaultdict(list)
    typ = dict()
    for line in data.strip().splitlines():
        n,ps = line.split('->')
        n = n.strip()
        if n not in ('broadcaster','output'):
            k,n = n[0],n[1:]
            typ[n] = k
        else:
            typ[n] = n[0]
        for p in ps.split(','):
            p = p.strip()
            par[p].add(n)
            chi[n].append(p)
    flops = {k:0 for k,t in typ.items() if t == '%'}
    cons = {k:{c:0 for c in par[k]} for k,t in typ.items() if t == '&'}
    
    probein = dict()
    fx = list(par[probe])
    while fx:
        p = fx.pop()
        if len(qs := par[p]) == 1:
            probein[p] = 0
        else:
            fx.extend(qs)
            
    wire = deque()
    def send(d, s, v):
        wire.append((d,s,v))
    def recv(d, s, v):
        # print(d, '<-', v, '<-', s)
        match typ.get(d, d):
            case '%':
                o = flops[d]
                if not v:
                    v = 0 if o else 1
                    flops[d] = v
                    for c in chi[d]:
                        send(c, d, v)
            case '&':
                cons[d][s] = v
                v = 0 if all(cons[d].values()) else 1
                for c in chi[d]:
                    send(c, d, v)
            case _:
                for c in chi.get(d, list()):
                  send(c, d, v)
    def cycle(t):
        send('broadcaster', None, 0)
        while wire:
            d,s,v = wire.popleft()
            recv(d,s,v)
            
            if (d in probein) and not any(cons[d].values()):
                probein[d] = t

    t = 0
    while not all(probein.values()):
        t += 1
        cycle(t)

    ans = math.prod(probein.values())
    return ans


data = '''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''
assert part1(data) == 32000000
data = '''
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''
assert part1(data) == 11687500


data = open('day20.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
