"""
import bisect
input()
scoreboard = sorted(set(map(int,input().split())),reverse=False)
input()
alice = list(map(int,input().split()))
for score in alice:
    if score not in scoreboard:
        bisect.insort(scoreboard,score)
    print(len(scoreboard)-scoreboard.index(score))
 """

import bisect
input()
scoreboard = sorted(set(map(int,input().split())),reverse=False)
input()
alice = list(map(int,input().split()))
for score in alice:
    print(len(scoreboard)-bisect.bisect_right(scoreboard,score)+1)


"""
7
100 100 50 40 40 20 10
4
5 25 50 120


6
4
2
1
"""
