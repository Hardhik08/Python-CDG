a = int(input())

if a%3==0:
    if a%5==0:
        print("Multiple of 3 and 5")
    else:
        print("Multiple of  only")
else:
    print("Not a multiple of 3")