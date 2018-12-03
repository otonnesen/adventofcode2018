#!/usr/bin/env python3

import sys

def main():
    lines = open(sys.argv[1]).readlines()
    grid = [[0 for i in range(1000)] for i in range(1000)]
    claims = [True for i in range(int(lines[-1].split()[0].strip('#'))+1)]
    for line in lines:
        for i in range(int(line.split()[3].split('x')[0])):
            for j in range(int(line.split()[3].split('x')[1])):
                x = i+int(line.split()[2].strip(':').split(',')[0])
                y = j+int(line.split()[2].strip(':').split(',')[1])
                ID = int(line.split()[0].strip('#'))
                if grid[x][y] != 0:
                    claims[ID] = False
                    claims[grid[x][y]] = False
                grid[x][y] = ID
    for i in range(1, len(claims)):
        if claims[i] == True:
            print(i)


if __name__ == '__main__':
    main()
