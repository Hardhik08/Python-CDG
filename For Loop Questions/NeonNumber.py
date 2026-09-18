n = int(input("Enter a number to check if a number is Neon or not:"))

a = n**2
count = 0

for i in str(a):
    count += int(i)
if count == n:
    print("It's a neon number")
else:
    print("Not a neon number")    
