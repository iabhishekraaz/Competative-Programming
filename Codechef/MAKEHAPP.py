# MAKEHAPP
for _ in range(int(input())):
    n,q=list(map(int,input().split()))
    s=0
    for i in range(q):
        l,r,v=list(map(int,input().split()))
        s+=(r-l+1)*v
        
    print(s)
