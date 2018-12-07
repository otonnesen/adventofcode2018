#!/usr/bin/env python3

import sys

def main():
    coords, dist, inf = [tuple((int(i.strip().replace(',','').split()[0]), int(i.strip().replace(',','').split()[1]))) for i in open(sys.argv[1]).readlines()], {}, set()
    for x in range(sorted(coords)[-1][0]):
        for y in range(sorted(coords, key=lambda x:x[1])[-1][1]):
            d = []
            for i in coords:
                d.append((abs(i[0]-x)+abs(i[1]-y), i))
            if sorted(d)[0][0] != sorted(d)[1][0]:
                if x == 0 or x == sorted(coords)[-1][0]-1 or y == 0 or y == sorted(coords, key=lambda x:x[1])[-1][1]-1:
                    inf.add(sorted(d)[0][1])
                dist[sorted(d)[0][1]] = 1 if sorted(d)[0][1] not in dist else 1 + dist[sorted(d)[0][1]]
    for i in sorted(dist, key=dist.get, reverse=True):
        if i not in inf:
            print(dist[i])
            break

if __name__ == '__main__':
    main()
