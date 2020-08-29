def CountFrequency(my_list):
    count = {} 
    for i in my_list: 
        count[i] = count.get(i, 0) + 1
    return count
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=CountFrequency(arr)
#     print(c)
    d=c.values()
#     print(d)
    e=CountFrequency(d)
#     f=e.values()
#     print(e)
#     q=[]
#     f.sort()
#     print("sort=",f)
#     for values in e.values():
#         print(values)
#         q.append(values)
#     print("q=",q)
#     print(e.values(3))
#     d=CountFrequency(c)
    ma=0
    r=10**5
    for j in e:
        if(e[j]>ma):
            ma=e[j]
            r=j
        elif(e[j]==ma):
            ma=e[j]
            r=min(r,j)
        else:
            r=r
    print(r)
