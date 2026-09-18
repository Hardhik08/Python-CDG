# Create a function to reverse a number.

def RevNum(n):

    if n == 0:
        return 0
    else:
        count = 0
        
        a = n % 10

        count += a
        

        return + count + RevNum(n//10)
a =  1236

k = RevNum(a)
print(k)