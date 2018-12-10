#!/usr/bin/env python3

import sys
import collections

def main():
    players, highscore = int(open(sys.argv[1]).readlines()[0].split()[0]), 100*int(open(sys.argv[1]).readlines()[0].split()[6])
    circle, cur, scores = collections.deque([0]), 0, [0 for i in range(players)]
    for i in range(1, highscore+1):
        if i%23 == 0:
            circle.rotate(7)
            scores[(i-1)%players] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    print(max(scores))

if __name__ == '__main__':
    main()
