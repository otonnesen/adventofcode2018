#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1]).readlines()
    lines.sort()
    ID = 0
    total = {}
    tmp = {}
    minutes = {}
    for i in lines:
        if i.split()[2] == 'Guard':
            ID = int(i.split()[3].strip('#'))
        if i.split()[2] == 'falls':
            tmp[ID] = int(i.split()[1][3:5])
            minutes[ID] = [0 for i in range(60)] if ID not in minutes else minutes[ID]
        if i.split()[2] == 'wakes':
            total[ID] = total[ID] + int(i.split()[1][3:5])-tmp[ID] if ID in total else 0
            for i in range(tmp[ID], int(i.split()[1][3:5])):
                minutes[ID][i] += 1
    print(max(total, key=total.get)*minutes[max(total, key=total.get)].index(max(minutes[max(total, key=total.get)])))
    

if __name__ == '__main__':
    main()
