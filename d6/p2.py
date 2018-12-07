#!/usr/bin/env python3

import sys

def main():
    s = 0
    coords = [tuple((int(i.strip().replace(',','').split()[0]), int(i.strip().replace(',','').split()[1]))) for i in open(sys.argv[1]).readlines()]
    for x in range(sorted(coords)[-1][0]):
        for y in range(sorted(coords, key=lambda x:x[1])[-1][1]):
            d = 0
            for i in coords:
                d += abs(i[0]-x)+abs(i[1]-y)
            if d < 10000:
                s += 1
    print(s)

if __name__ == '__main__':
    main()
