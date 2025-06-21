#Q3

print('Enter no for exit')
print('enter yes to run the code')
while True:
    b=input('Enter yes or no: ')
    if b=='yes':
        a=str(input('Enter the string: '))
        if a==a[::-1]:
            print(a[::-1],'is a palindrome')
        elif a!=a[::-1]:
            print(a[::-1],'is not a palindrome')
    elif b=='no':
        break
