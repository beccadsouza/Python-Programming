n, k = map(int, input().split())
string = input()
answer = left = right = []
left = [x for x in string[:n // 2]]
if n % 2 == 0: right = [x for x in string[n // 2:][::-1]]
else: right = [x for x in string[n // 2 + 1:][::-1]]
diff = sum([1 for x, y in zip(left, right) if x != y])
if diff > k: print(-1)
else:
    poss = k - diff
    start = 0
    while poss > 0 and start != n // 2:
        if left[start] != right[start]:
            if left[start] == '9' or right[start] == '9':
                if left[start] == '9':
                    right[start] = '9'
                else:
                    right[start] = '9'
            if left[start] != '9' and right[start] != '9':
                left[start] = '9'
                right[start] = '9'
                poss -= 1
        if left[start] == right[start]:
            if left[start] != '9' and poss >= 2:
                left[start] = '9'
                right[start] = '9'
                poss -= 2
        start += 1
    while start != n // 2:
        if left[start] > right[start]:right[start] = left[start]
        else:left[start] = right[start]
        start += 1
    if poss > 0 and n % 2 == 1:answer = left[:] + ['9'] + left[::-1]
    elif n % 2 == 1:answer = left + [string[n // 2]] + left[::-1]
    else:answer = left + left[::-1]
    print("".join(answer))
