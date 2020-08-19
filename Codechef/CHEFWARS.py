#----------------------CODE-------------------#
#-----------------------BY-------------------#
#-------------------ABHISHEK RAJ-------------------#
for i in range(int(input())):
    d,c=[int(x) for x in input().split()]
#     print(d,c)
    while (d>0 and c>0):
        d=d-c
#         print('d',d)
        c=(c//2)
#         print('c',c)
    if c==0 and d<=0:
        print("1")
    elif c==0:
        print("0")
    elif d<=0:
        print("1")

        
