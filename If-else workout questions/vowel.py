# Take a character input and check if it is a vowel or consonant.

alpha = input()

vowels = ['a','e','i','o','u']

if alpha.lower() in vowels:
    print("It is a vowel")
else:
    print("A consonent")