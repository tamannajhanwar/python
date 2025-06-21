#Q2

def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return(f)
b=int(input('Enter the number: '))
print(factorial(b))