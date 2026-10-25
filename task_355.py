n = float(input('Enter number: '))
index = str(n).index('.')
for i in str(n):
    if i == '.':
        print(str(n)[int(index) + 1])
        