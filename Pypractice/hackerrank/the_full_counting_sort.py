hm = dict([(x,' ') for x in range(101)])
n = int(input())
for i in range(n):
    x,s = input().split()
    if i in range(n//2):
        hm[int(x)] += '- '
    else:
        hm[int(x)] += s + ' '
print("".join(hm.values()))
