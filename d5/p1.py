#!/usr/bin/env python3

import sys
import string
import time

def main():
    line = list(open(sys.argv[1]).readlines()[0].strip())
    diff = 1
    while diff != 0:
        diff = 0
        i = 0
        while i < len(line)-1:
            if (line[i] in string.ascii_lowercase and line[i].upper() == line[i+1]) or (line[i] in string.ascii_uppercase and line[i].lower() == line[i+1]):
                del line[i]
                del line[i]
                diff += 1
            else:
                i += 1
    print(len(line))

if __name__ == '__main__':
    main()
