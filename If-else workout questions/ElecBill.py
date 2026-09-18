n = int(input())

if 0<=n<=100:
    print(f"Total bill amount is: {n*2:.0f}")
elif 101<=n<=200:
     print(f"Total bill amount is: {n*3:.0f}")
elif 201<=n<=300:
      print(f"Total bill amount is: {n*5:.0f}")
else:
      print(f"Total bill amount is: {n*7:.0f}")
