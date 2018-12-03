#!/usr/bin/env python3

import sys

def isNeighbor(s1, s2):
    if s1 == s2:
        return False
    if len(s1) != len(s2):
        return False

    diff = False
    index = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:
                return False
            diff = True
            index = i
    ret = [diff, index]
    return ret

def main():
    lines = open(sys.argv[1]).readlines()
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            n = isNeighbor(lines[i], lines[j])
            if n:
                print(lines[i][:n[1]]+lines[i][n[1]+1:-1])

if __name__ == '__main__':
    main()
