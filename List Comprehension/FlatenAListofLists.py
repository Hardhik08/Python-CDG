# Flatten a list of lists into a single list

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [i for j in x for i in j]
print(y)