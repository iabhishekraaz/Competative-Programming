# Q.2 ARRGAME
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.append(1)
    k=0
    arr1=[]
    for i in range(0,n+1):
#         print("arr[i]=",arr[i])
        if arr[i]==0:
#             print("~~~~~")
            k+=1
        else:
            if k>0:
                arr1.append(k)
            k=0
    print(arr1)
    arr1.sort(reverse=True)
    print(arr1)
    m=len(arr1)
    print("m=",m)
    if m==0:
        print("No")
    if m==1:
        if arr[m]%2==0:
            print("No")
        else:
            print("Yes")
    if m>=2:
#         print("")
        if arr1[0]%2==0:
            print("No")
        else:
            z=arr1[0]+1//2
            if z<=arr[1]:
                print("No")
            else:
                print("Yes")
