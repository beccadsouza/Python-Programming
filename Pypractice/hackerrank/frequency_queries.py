d = {}
for _ in range(int(input())):
    op,x = map(int,input().split())
    if op is 1:
        if x in d.keys(): d[x] += 1
        else: d[x] = 1
    elif op is 2 and x in d.keys(): d[x] -= 1
    elif op is 3: print(1 if x in d.values() else 0)
