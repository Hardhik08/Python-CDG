# Create a function to check whether a number is palindrome.

def Pali(n):
    b = str(n)
    if b[::1] == b[-1::-1]:
        return True
    else:
        return False

a = 12343216

k = Pali(a)

print(k)