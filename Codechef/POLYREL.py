t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=[]
    for i in range(n):
        x,y=map(int,input().split())
        a.append(x)
        a.append(y)
    s=n
    m=n//2
    while m>=3:
        s=s+m
        m=m//2

    print(s)
        
