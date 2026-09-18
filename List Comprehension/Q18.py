# Create a list comprehension to reverse the order of words in a sentence

x = "Python is a very interesting programming lang. Everyone must learn it"

r = [i for i in x.split()]
print(r[::-1])
