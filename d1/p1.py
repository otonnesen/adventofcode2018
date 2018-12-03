#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1])
    s = 0
    for i in lines.readlines():
        if i[0] == '-':
            s -= int(i[1:])
        else:
            s += int(i[1:])
    print(s)

if __name__ == '__main__':
    main()
