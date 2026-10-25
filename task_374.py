wrd1 = str(input('Enter first word: ')).strip()
wrd2 = str(input('Enter second word: ')).strip()

possible = True
for chr in wrd2:
    if wrd2.count(chr) > wrd1.count(chr):
        possible = False
        break
if possible:
    print('Yes')
else:
    print('No')
