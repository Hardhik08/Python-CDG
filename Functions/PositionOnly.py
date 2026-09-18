def Greet(a,b,/):
    print(a,b)

Greet(20,20) # No error
print("Error is:")
Greet(20,b=20) # Gives error

