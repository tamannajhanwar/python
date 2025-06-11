#Q3

print('Enter 1 for addition')
print('Enter 2 for subtraction')
print('Enter 3 for multiply')
print('Enter 4 for division')
print('Enter 5 for floor division')
print('Enter 6 for modulus')
print('Enter 7 for exponentiation')
print('Enter 0 for exit')

while True:
    
    a=int(input('Enter first value: '))
    b=int(input('Enter second value: '))
    c=int(input('Enter the number: '))

    if c==1:
        print('The addition is: ', a+b)
    if c==2:
        print('The subtraction is: ', a-b)
    if c==3:
        print('The multiply is: ', a*b)
    if c==4:
        print('The division is: ', a/b)
    if c==5:
        print('The floor division is: ', a//b)
    if c==6:
        print('The modulus is: ', a%b)
    if c==7:
        print('The exponentiation is: ', a**b)
    if c==0:
        break
