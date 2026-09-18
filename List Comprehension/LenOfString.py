# Filter strings with more than five characters from a list of strings.?

a = ['HelloAbc','Ram','How Are','You','Whatsup']
x = [i for i in a if len(i)>5]
print(x)