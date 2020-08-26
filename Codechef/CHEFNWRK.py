for _ in range(int(input())): 
    n,k=[int (x) for x in input().split()]
    d=0
    a=0
    f=0
    
    w=list(map(int,input().split()))
    for l in range(n):
#         print("w[l]=",w[l])
        a=a+w[l]
        if (w[l]>k):
            print("-1")
            f=1
            break
        if (a>k):
            d=d+1
            a=w[l]
    if f!=1:
        print(d+1)
