#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1]).readlines()
    grid = [[0 for i in range(1000)] for i in range(1000)]
    s = 0
    for line in lines:
        for i in range(int(line.split()[3].split('x')[0])):
            for j in range(int(line.split()[3].split('x')[1])):
                grid[i+int(line.split()[2].strip(':').split(',')[0])][j+int(line.split()[2].strip(':').split(',')[1])] += 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 1:
                s += 1
    print(s)


if __name__ == '__main__':
    main()
