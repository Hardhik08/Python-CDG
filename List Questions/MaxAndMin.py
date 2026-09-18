l = [1,2,3,4,5,6,7,8,9]

print(max(l))
print(min(l))

max_num = l[0]
min_num = l[0]

for i in l:
	if max_num<i:
		max_num = i
	if min_num>i:
		min_num=i
print(max_num,"Max")
print(min_num,"Min")