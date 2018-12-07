#!/usr/bin/env python3

import sys
import string

def main():
    G = {i:[] for i in string.ascii_uppercase}
    times = dict(zip((string.ascii_uppercase), range(61,87)))
    time = 0
    jobs = set()
    for i in open(sys.argv[1]).readlines():
        G[i.split()[7]].append(i.split()[1])
    while G:
        while len(list(filter(lambda x: len(G[x]) == 0 and x not in jobs, G))) != 0 and len(jobs) <= 5:
            jobs.add(min(list(filter(lambda x: len(G[x]) == 0 and x not in jobs, G))))
        n = min(jobs, key=lambda x: times[x])
        for i in range(times[n]):
            time += 1
            for j in jobs:
                times[j] -= 1
        del G[n]
        jobs -= set(n)
        for i in G:
            G[i] = list(filter(lambda x: x != n, G[i]))
    print(time)

if __name__ == '__main__':
    main()
