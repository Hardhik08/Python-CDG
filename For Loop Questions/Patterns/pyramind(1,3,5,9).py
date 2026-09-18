r = 9

for i in range(1,r+1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range(1,i-1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

