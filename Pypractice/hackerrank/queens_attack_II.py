n,k = map(int,input().split())
rq,cq = map(int,input().split())
obstacles = [tuple(int(x) for x in input().split()) for x in range(k)]
row = []
col = []
ndiag = []
pdiag = []
for obs in obstacles:
    if rq-obs[0] == cq-obs[1]:pdiag.append(obs)
    if rq - obs[0] == obs[1]-cq:ndiag.append(obs)
    if obs[0] == rq :row.append(obs)
    if obs[1] == cq :col.append(obs)


col.extend([(1,cq),(n,cq)])
row.extend([(rq,1),(rq,n)])

r_nmax,c_nmax = rq,cq
r_pmin,c_pmin = rq,cq

r_pmax,c_pmax = rq,cq
r_nmin,c_nmin = rq,cq

while r_nmax != n and c_nmax!= 1:
    r_nmax += 1
    c_nmax -= 1
while r_pmin != 1 and c_pmin != 1:
    r_pmin -= 1
    c_pmin -= 1
while r_pmax != n and c_pmax!= n:
    r_pmax += 1
    c_pmax += 1
while r_nmin != 1 and c_nmin != n:
    r_nmin -= 1
    c_nmin += 1

pdiag.extend([(r_pmax,c_pmax),(r_pmin,c_pmin)])
ndiag.extend([(r_nmax,c_nmax),(r_nmin,c_nmin)])
print(ndiag,pdiag,row,col,sep='\n')



if len(pdiag) ==2:
    print()
