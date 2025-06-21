#Q3

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a>b:
    if a>c:
        print(a,'is largest')
    elif a<c:
        print(c,' is largest')
elif b>a:
    if b>c:
        print(b,'is largest')
    elif b<c:
        print(c,'is largest')
elif c>a:
    if c>b:
        print(c,'is largest')
    if c<b:
        print(b,'is largest')
