# Create a function to calculate factorial

def Fact(n):
    if n == 1:
        return 1
    return n * Fact(n-1)

k = 6

a = Fact(k)

print(a)