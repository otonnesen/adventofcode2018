#!/usr/bin/env python3

import sys
import string
import time

def main():
    line = open(sys.argv[1]).readlines()[0].strip()
    l = len(line)
    for i in string.ascii_lowercase:
        print(i)
        diff = 1
        tmp = list(line.replace(i,'').replace(i.upper(),''))
        while diff != 0:
            diff = 0
            i = 0
            while i < len(tmp)-1:
                if (tmp[i] in string.ascii_lowercase and tmp[i].upper() == tmp[i+1]) or (tmp[i] in string.ascii_uppercase and tmp[i].lower() == tmp[i+1]):
                    del tmp[i]
                    del tmp[i]
                    diff += 1
                else:
                    i += 1
        l = len(tmp) if len(tmp) < l else l
    print(l)

if __name__ == '__main__':
    main()
