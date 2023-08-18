import sys

print('Welcome to the Python Calculator')

print('''Operations you can do are:
Addition
Subtraction
Multiplication
Division
''')


an = input('Which operation would you like to do: ')
di = float(input('What is the first digit: '))
dii = float(input('What is the second digit: '))

if an == 'Addition':
    print('Your answer is', di + dii)

elif an == 'Subtraction':
    print('Your answer is', di - dii)

elif an == 'Multiplication':
    print('Your answer is', di * dii)

elif an == 'Division': 
    print('Your answer is', di / dii)

else:
    print('Oops that was an Invalid Operation')
    sys.exit()