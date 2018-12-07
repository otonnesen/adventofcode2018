#!/usr/bin/env python3

import sys
import string

def main():
    G = {i:[] for i in string.ascii_uppercase}
    for i in open(sys.argv[1]).readlines():
        G[i.split()[7]].append(i.split()[1])
    L = ''
    while G:
        n = min(list(filter(lambda x: len(G[x]) == 0, G)))
        del G[n]
        for i in G:
            G[i] = list(filter(lambda x: x != n, G[i]))
        L += n
    print(L)
        

if __name__ == '__main__':
    main()
