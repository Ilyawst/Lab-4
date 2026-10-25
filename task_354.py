consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'

ltr1 = input('Enter first letter: ')
ltr2 = input('Enter second letter: ')

if ltr1.lower() in consonant:
    print(f'{ltr1} is a consonant')
else:
    print(f'{ltr1} is a vowel')

if ltr2.lower() in consonant:
    print(f'{ltr2} is a consonant')
else:
    print(f'{ltr2} is a vowel')
