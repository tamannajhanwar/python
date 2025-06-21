#Q4

print('Enter + for addition')
print('Enter - for subtract')
print('Enter * for multiply')
print('Enter / for divide')
print('enter e for exit')
while True:
    
    a=int(input('Enter first value: '))
    b=int(input('Enter second value: '))
    c=input('Enter the operator: ')
    
    if c=='+':
        print('Addition is',a+b)
    elif c=='-':
        print('Subtract is',a-b)
    elif c=='*':
        print('Multiply is',a*b)
    elif c=='/':
        print('divide is',a/b)
    elif c=='e':
        break
