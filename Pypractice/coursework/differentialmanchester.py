code = input()
d = {1:'10',0:'01'}
for start in [0,1]:
    print("start voltage : ",start)
    answer = ""
    if code[0] == '1': answer += d[start]
    else: answer += d[(start+1)%2]
    for x in code[1:]:
        if x=='0': answer += answer[-2:]
        else : answer += answer[-2:][::-1]
    print("encoding : ",str(start)+answer)
