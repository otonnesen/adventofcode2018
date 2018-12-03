#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1])
    s = 0
    changes = []
    for i in lines.readlines():
        if i[0] == '-':
            s = -1*int(i[1:])
        else:
            s = int(i[1:])
        changes.append(s)
    
    d = set()
    i = 0
    s = 0
    while s not in d:
        d.add(s)
        s += changes[i%len(changes)]
        i += 1
    print(s)



if __name__ == '__main__':
    main()
