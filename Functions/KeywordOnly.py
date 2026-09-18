def Hello(*,a,b):
    print(a,b)

Hello(a="Hardhik",b="Age is 21") # Gives no error

Hello("Hardhik",b = 20) # Gives error 
# Error is 
'''
Traceback (most recent call last):
  File "c:\Users\hardh\OneDrive\Documents\VS CODE\Python\Functions\KeywordOnly.py", line 6, in <module>
    Hello("Hardhik",b = 20) # Gives error
    ~~~~~^^^^^^^^^^^^^^^^^^
TypeError: Hello() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

'''