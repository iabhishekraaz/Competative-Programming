#----------------------CODE-------------------#
#-----------------------BY-------------------#
#-------------------ABHISHEK RAJ-------------------#
for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    p=list(map(int,input().split()))[:n]
    arr=[]
    for j in range(n):
        if k%p[j]==0:
            arr.append(p[j])
    if len(arr)==0:
        print("-1")
    else:
        arr.sort(reverse=True)
        print(arr[0])
