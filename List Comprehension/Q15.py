# Calculate the cumulative sum of a list of numbers using a list comprehension

x = [1,2,3,4,5,6]

r = [sum(x[:i]) for i in x]
print(r)

