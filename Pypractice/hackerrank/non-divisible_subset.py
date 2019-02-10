from itertools import permutations


def isNotMaximal( l ):
    global remove, k
    neg = False
    tup = list(permutations(l, 2))
    temp = [tup.remove((x[1], x[0])) for x in tup]
    # print(tup)
    for t in tup:
        if sum(t) % int(k) == 0:
            remove.extend([t[0], t[1]])
            # print(remove,"in func")
            neg = True
    return neg


_, k = input().split()
l = list(map(int, input().split()))
remove = []
while (isNotMaximal(l)):
    remove = sorted(remove, key=remove.count, reverse=True)
    # print(remove[0],"highest freq rn")
    l.remove(remove[0])

print(len(l))
