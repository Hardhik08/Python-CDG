# Take an integer input from the user and print whether it is positive or negative.


'''taking input from the user'''
a = int(input()) 

'''use if to check if the number is positive or negative'''
if a>0:
    print("The registered number is positive")

    '''use else so that the controller will move to this block to check when the IF BLOCK is FAILED'''
else:
    print("The registered number is negative")