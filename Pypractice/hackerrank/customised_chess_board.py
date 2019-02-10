t = int(input())
for testcase in range(t):
    n = int(input())
    grid = []
    flag = True
    for row in range(n):
        grid.append(input().split())
    print(n,len(grid))
    for row in grid:
        print(row)
        if set(row[::2]) == set(row[1::2]) and row!=[]:
            print("happened heree",row)
            print(row[::2],row[::-2])
            flag = False
            break
    if flag:
        for column in range(n):
            col = [row[column] for row in grid]
            print(col)
            if set(col[::2]) == set(col[1::2]) and col!=[]:
                print("happened here",col)
                flag = False
                break
    if not flag:
        print('No')
    else: print('Yes')

