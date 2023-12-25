#!/usr/bin/env python
from collections import defaultdict, deque, Counter


def part1(data):
    nodes = defaultdict(set)
    for line in data.strip().splitlines():
        a,ps = line.split(':')
        for b in ps.split():
            nodes[a].add(b)
            nodes[b].add(a)
    stat = Counter()
    for start in nodes.keys():
        fringe = deque([(start, list())])
        seen = set()
        while fringe:
            p,path = fringe.popleft()
            if p in seen: continue
            seen.add(p)
            for k in path:
                stat[k] += 1
            for x in nodes[p]:
                k = tuple(sorted([p,x]))
                fringe.append((x, path+[k]))
    cut = stat.most_common()[:3]
    for (a,b),_ in cut:
        nodes[a].discard(b)
        nodes[b].discard(a)
    seen = set()
    fringe = [a]
    while fringe:
        p = fringe.pop()
        if p in seen: continue
        seen.add(p)
        for x in nodes[p]:
            fringe.append(x)
    ans = len(seen) * (len(nodes) - len(seen))
    return ans


data = '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''
assert part1(data) == 54


data = open('day25.in').read()
print('part1:', part1(data))
