#This is slicing program
a = "Hardhik"
#Below prints the individual characters
print("To print individual characters. This is positive slicing. moves from left to right")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])


#TO print a portion of a string
print("To print a portion of a string")
print(a[0:2])
print(a[2:4])
print(a[4:6])
print(a[6:8])

#To print the last character
print("To print the last character. This is negative slicing. moves from right to left")
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])
print(a[-7])

#Negative slicing
print("Negative slicing")
print(a[-7:-1])
print(a[-7:-2])
print(a[-7:-3])
print(a[-7:-4])
print(a[-7:-5])
print(a[-7:-6])
print(a[-7:-7])

#Step slicing
print("Step slicing")
print(a[0:8:2], "Used step size of 2, print every second character")