#  Iterate over a dictionary and print key-value pairs using a for loop

d = {1:"Name", 2:"Name1", 3:"Name2", 4:"Name3"}

for i in range(len(d)):
    print(list(d.items())[i])

# Notes:

# If you use len(dic), you will get error (typeError) use "range(len(d))"



