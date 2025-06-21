#Q5

a=str(input('Enter the string: '))
f={c:a.count(c) for c in set(a)}
print(f)