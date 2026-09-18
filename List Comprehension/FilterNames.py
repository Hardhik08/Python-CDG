# Filter names that start with the letter "A" from a list of names.

x = ["Apple","ball",'Aryan',"America","Africa",'aman']

r = [i for i in x if i.startswith("A") or i.startswith("a")]
print(r)