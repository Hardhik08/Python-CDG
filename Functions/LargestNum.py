# Create a function to find the largest element in a list

def Large(n):
    return max(n)

a = list(map(int, input().split(",")))
k = Large(a)

print(k)