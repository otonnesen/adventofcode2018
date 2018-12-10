#!/usr/bin/env python3

import sys

def main():
    tokens = open(sys.argv[1]).readlines()[0].split()
    print(parse(tokens, 0)[1])

def parse(tokens, index):
    children, metadata, s = int(tokens[index]), int(tokens[index+1]), 0
    index += 2
    for i in range(children):
        t = parse(tokens, index)
        index = t[0]
        s += t[1]
    for i in range(metadata):
        s += int(tokens[index])
        index += 1
    return (index, s)


if __name__ == '__main__':
    main()
