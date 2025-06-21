#Q2

a=int(input('Enter your age: '))
if a>=0:
    if a<=12:
        print('You are a child')
    elif a>12 and a<=19:
        print('You are a teenager')
    elif a>19 and a<=59:
        print('You are an adult')
    elif a>59:
        print('You are a senior')
else:
    print('This age is not valid')
