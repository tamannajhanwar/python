#Q4

def s():
    n=str(input('Enter the string: '))
    c={c:n.count(c) for c in n.split()}
    return(c)
print(s())