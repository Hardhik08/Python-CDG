# Create a list comprehension to find the squares of even numbers and cubes of odd numbers in a given list of integers

x = [i**2 if i %2==0 else i**3 for i in range(10) ]
print(x)