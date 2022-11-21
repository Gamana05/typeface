def check(s,l):
    while(l>0):
        r=l%10
        if r not in s:
            return False
        l=l//10
    return True
            
n=int(input())
i=1
t=1
s=[0,1,2,5,6,8,9]
while(t<=n):
    if check(s,i):
        t+=1
    i+=1
print(i-1)