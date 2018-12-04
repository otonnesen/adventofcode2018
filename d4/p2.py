#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1]).readlines()
    lines.sort()
    ID = 0
    start = 0
    minutes = {}
    for i in lines:
        if i.split()[2] == 'Guard':
            ID = int(i.split()[3].strip('#'))
        if i.split()[2] == 'falls':
            start = int(i.split()[1][3:5])
            minutes[ID] = [0 for i in range(60)] if ID not in minutes else minutes[ID]
        if i.split()[2] == 'wakes':
            for i in range(start, int(i.split()[1][3:5])):
                minutes[ID][i] += 1

    print(max(minutes, key=lambda x:max(minutes[x]))*minutes[max(minutes, key=lambda x:max(minutes[x]))].index(max(minutes[max(minutes, key=lambda x:max(minutes[x]))])))

if __name__ == '__main__':
    main()
