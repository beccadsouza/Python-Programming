#    Created by Rebecca Dsouza on 22/6/18
input()
scores = []
integers = set(map(int, input().split())) 
bits = len('{0:b}'.format(max(integers)))
integers = list((map(lambda x: '{0:b}'.format(x).zfill(bits), integers)))
if len(integers) == 1: print(integers[0])
else:
    while len(set([x[0] for x in integers])) == 1:
        integers = [x[1:] for x in integers]
    low = list(filter(lambda x: x[0] == '0', integers))
    high = list(filter(lambda x: x[0] == '1', integers))
    for x in low:
        for y in high:
            scores.append(int(x,2)^int(y,2))
    print(min(scores))
