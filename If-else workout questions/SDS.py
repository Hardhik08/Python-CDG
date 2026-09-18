n = int(input("Enter your amount:"))

if n>=5000:
    print(f"Final amount after 20% discount is {n-(n*0.2):.0f}")
elif 5000>n>=3000:
    print(f"Final amount after 10% discount is {n-(n*0.1):.0f}")
elif 3000>n>=1000:
    print(f"Final amount after 5% discount is {n-(n*0.05):.0f}")
else:
    print("Shop more to get discount")