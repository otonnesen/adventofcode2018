#!/usr/bin/env python3

import sys

class Tree:
    def __init__(self):
        self.children, self.metadata = [], []
    def value(self):
        return sum(self.metadata) if len(self.children) == 0 else sum([i.value() for i in [self.children[i-1] for i in list(filter(lambda x: x-1 < len(self.children) and x != 0, self.metadata))]])

def main():
    tokens = open(sys.argv[1]).readlines()[0].split()
    print(parse(tokens, 0)[1].value())

def parse(tokens, index):
    T = Tree()
    children, metadata = int(tokens[index]), int(tokens[index+1])
    index += 2
    for i in range(children):
        t = parse(tokens, index)
        index = t[0]
        T.children.append(t[1])
    for i in range(metadata):
        T.metadata.append(int(tokens[index]))
        index += 1
    return (index, T)


if __name__ == '__main__':
    main()
