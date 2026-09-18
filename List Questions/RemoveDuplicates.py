l = list(input().split())
unq_num = []
num = set()


for i in l:
	if i not in num:
		unq_num.append(i)
		num.add(i)
		
print(unq_num)