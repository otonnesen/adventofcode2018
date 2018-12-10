#!/usr/bin/env python3

import sys

def main():
    players, highscore = int(open(sys.argv[1]).readlines()[0].split()[0]), int(open(sys.argv[1]).readlines()[0].split()[6])
    circle, cur, scores = [0], 0, [0 for i in range(players)]
    for i in range(1, highscore+1):
        if i%23 == 0:
            cur = (cur-7)%len(circle)
            scores[(i-1)%players] += i + circle[cur]
            circle = circle[:cur] + circle[cur+1:]
        else:
            cur = (cur+2)%len(circle)
            circle.insert(cur, i)
    print(max(scores))

if __name__ == '__main__':
    main()
