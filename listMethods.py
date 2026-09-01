a = [1,2,3,4,5,6,7]

print("List can store elements of different DTypes, for example:")
b = [1,2.5,"Hardhik",True]
print(b)

# Methods to perform on List:
# append()  --> adds an element at the end of the list
# clear()   --> removes all the elements from the list
# copy()    --> returns a copy of the list
# count()   --> returns the number of times an element occurs in the list
# extend()  --> adds all the elements of a list to the current list
# index()   --> returns the index of the first occurrence of an element in the list
# insert()  --> inserts an element at a specified index in the list
# pop()     --> removes and returns the element at a specified index in the list
# remove()  --> removes the first occurrence of an element from the list
# reverse() --> reverses the order of the elements in the list
# sorted()  --> returns a sorted copy of the list
# sum()     --> returns the sum of all the elements in the list
print(a, "Homogeneous List, methods are performed on this list as of now\n")
"""Append()"""
a.append(8)
print(a," --> This is append method, adds an element at the **end** of the list\n")

'''clear()'''
a.clear()
print(a," --> This is clear method, removes all the elements from the list\n")

a=[1,2,3,4,5,6,7]

'''copy()'''
b = a.copy()
print(b," --> This is copy method, returns a copy of the list. Shares only content, not the address \n")

'''count()'''
a = [1,2,3,4,5,5,5,6,8,0,"Hii"]
print(a, "count of occurences of 5:",a.count(5)," --> This is count method, returns the number of times an element occurs in the list\n")

'''pop()'''
a.pop(2)
print(a," --> This is pop method, removes and returns the element at a specified index in the list\n")

'''remove()'''
a.remove(5)
print(a," --> This is remove method, removes the first occurrence of an element from the list\n")

'''reverse()'''
a.reverse()
print(a," --> This is reverse method, reverses the order of the elements in the list\n")

'''sorted()'''
a = [1,2,10,15,13,100,12,14,16]
print(a, "Sorted List:",sorted(a)," --> This is sorted method, returns a sorted copy of the list\n")

'''sum()'''
a = [1,2,10,15,13,100,12,14,16]
print(a, "Sum of all elements:",sum(a)," --> This is sum method, returns the sum of all the elements in the list\n")
