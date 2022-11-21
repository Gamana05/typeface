l=[]
for i in range(257):
    l.append(list(map(int,input().split())))
rm=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]==0:
            t=[]
            t.append(i)
            t.append(j)
            rm.append(t)
hl=rm[0][0]
hh=rm[0][0]
vl=rm[1][1]
vh=rm[1][1]
for i in rm:
    if i[0]>hh:
        hh=i[0]
    if i[0]<hl:
        hl=i[0]
    if i[1]<vl:
        vl=i[1]
    if i[1]>vh:
        vh=i[1]
print(hl,vl)
print(hl,vh)
print(hh,vl)
print(hh,vh)