# Count the number of vowels in a string using a for loop

vow = "aeiou"

a = input()

count = 0

for i in a:
    if i in vow:
        count +=1
        print(i)
print(f"There are {count} vowel(s) in {a}")


