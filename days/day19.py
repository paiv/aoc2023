#!/usr/bin/env python
import math
import re


def part1(data):
    rules,parts = data.strip().split('\n\n')
    def genop(s):
        (n,o,x), = re.findall(r'(\w+)([<>])(\w+)', s)
        x = int(x)
        match o:
            case '<':
                return (lambda o: o[n] < x)
            case '>':
                return (lambda o: o[n] > x)
    def gencd(s):
        if ':' in s:
            q,n = s.split(':')
            f = genop(q)
            return (lambda o: n if f(o) else None)
        return (lambda _: s)
    def genflow(s):
        checks = [gencd(q) for q in s.split(',')]
        def flow(o):
            for q in checks:
                if (n := q(o)):
                    return n
        return flow
    rules = {n:genflow(s[:-1])
        for line in rules.split() for n,s in [line.split('{')]}
    ans = 0
    for line in parts.split():
        part = {a:int(b) for p in line[1:-1].split(',') for a,b in [p.split('=')]}
        pos = 'in'
        while pos not in 'AR':
            op = rules[pos]
            pos = op(part)
        if pos == 'A':
            ans += sum(part.values())
    return ans


def part2(data):
    rules,_ = data.strip().split('\n\n')
    def pflow(rs):
        res = list()
        for s in rs.split(','):
            (k,o,x,r), = re.findall(r'(?:(\w+)([<>])(\w+)[:])?(\w+)', s)
            if k:
                cx = (k, o, int(x))
                rule = (cx, r)
            else:
                rule = (None, r)
            res.append(rule)
        return res
    rules = {n:pflow(rs) for line in rules.split() for n,rs in [line[:-1].split('{')]}
    ns = 'xmas'
    def go(name, checks):
        if name == 'A':
            return [[range(1,4001) for _ in range(len(ns))]]
        if name == 'R':
            return []
        q,t = checks[0]
        if not q:
            return go(t, rules.get(t))
        k,o,x = q
        i = ns.index(k)
        res = list()
        ws = go(t, rules.get(t))
        for rs in ws:
            nl = list(rs)
            r = nl[i]
            match o:
                case '<':
                    nl[i] = range(r.start, min(x,r.stop))
                case '>':
                    nl[i] = range(max(x+1,r.start), r.stop)
            res.append(nl)
        ws = go(name, checks[1:])
        for rs in ws:
            nl = list(rs)
            r = nl[i]
            match o:
                case '<':
                    nl[i] = range(max(x,r.start), r.stop)
                case '>':
                   nl[i] = range(r.start, min(x+1,r.stop))
            res.append(nl)
        return res
    ranges = go('in', rules['in'])
    ans = sum(math.prod(map(len, rs)) for rs in ranges)
    return ans


data = '''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''
assert part1(data) == 19114
assert part2(data) == 167409079868000


data = open('day19.in').read()
print('part1:', part1(data))
print('part2:', part2(data))
