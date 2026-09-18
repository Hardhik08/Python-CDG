# Create a function to count vowels in a string.


def Vowels(a):
    count = 0
    for i in a:
        if i in "aeiou":
            count += 1
    return count
    
a = "aeiou"

k = Vowels(a)
print(k)
