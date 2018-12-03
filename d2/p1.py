#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1])
    two = 0
    three = 0
    for line in lines.readlines():
        letters = [0 for i in range(26)]
        for c in line[:-1]:
            letters[ord(c)-97] += 1
        two += 1 if 2 in letters else 0
        three += 1 if 3 in letters else 0
    print(two * three)

if __name__ == '__main__':
    main()
