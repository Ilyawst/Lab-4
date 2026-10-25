formula = input('Enter expression: ')

parenthesis_count = 0
for chr in formula:
    if chr == '(':
        parenthesis_count += 1
    if chr == ')':
        parenthesis_count -= 1
    if parenthesis_count < 0:
        break

if parenthesis_count == 0:
    print('True')
else:
    print('False')
