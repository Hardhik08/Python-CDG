# Create a function to reverse a number.

def RevNum(n):

    if n == 0:
        return 0
    else:
        
        a = n % 10

        count = a * (10 ** (len(str(n)) - 1))
        # print("n =", n, "a =", a, "digits =", len(str(n)))
        # print("count =", count)
        

        return + count + RevNum(n//10)
a = 9876543210

k = RevNum(a)
print(k)