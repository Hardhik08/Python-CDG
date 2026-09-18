# Filter out duplicates from a list using a list comprehension

x = [1,2,3,12,2,2,4,5,6,4,4,3,2,10,1,15,"hello",'hardhik','hello',"Hello"]

r = [j for i,j in enumerate(x) if j not in x[:i]]

print(r)