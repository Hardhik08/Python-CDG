import random as r

while True:     # Used Loop so that the guessing runs till the user 
    a = int(input("Enter a number between 1 and 10, Enter 11 to exit:\n"))

    b = r.randint(1,10)


    if a==b:
        print("Guessed the correct number")
        break
    if 11 == a:
        break
    else:
         print(b,"This was the number")