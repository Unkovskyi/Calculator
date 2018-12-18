import string
from string import whitespace, punctuation

from function import * #импорт функций и листа операций

# начало програмы

Flaf = False
while Flaf == False:
    name = input('input yor name: ')
    if name in string.punctuation or name == ' ':
        print('  !!!  invalid input please repeat')
    else:
        Flaf = True
print('Hello, ', name)

start = 'y'
while start == 'y':
    start = input('Do you want to calculate?    [y]-yes, [any  button]-no:  ')
    if start == 'y':
        flag = True
        while flag:
            try:
                number_1 = float(input('input number 1:  '))
                number_2 = float(input('input number 2:  '))
                oper = input('input operation from the list {}: '.format(list(list_of_oper.keys()))).strip()
                flag = False
            except(ValueError) as e:
                print('!!! Error1:', e)
                print('Try again')

            res = None
        if oper in list(list_of_oper.keys()):
            res = list_of_oper[oper](number_1, number_2)
            print('Result:  {} {} {}={}'.format(number_1, oper, number_2, res))
        else:
            print('sorry, this operation is not in the list, try again ')
print('Ok, byе')