n = int(input())

if n>= 2000:
    print(f"Final price: {n}")
elif 2000>n>=1000:
    print(f"Final price: {n+50:.0f}")
else:
    print(f"Final price: {n+100:.0f}")