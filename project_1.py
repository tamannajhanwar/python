#description of the program
print('''Hello and welcome to the interactive personal data collector!
This collector collects your information and proides it to you in a systematic way
It also prints the type and memory address of the variable
and also it prints you your birth year according to your age''')

print(end='\n')
print(end='\n')
print(end='\n')

#collecting info from user
a=str(input('Enter your name: '))
b=int(input('Enter your age: '))
c=float(input('Enter your height: '))
d=int(input('Enter your favorite number: '))
e=int(input('Enter the current year: '))
f=e-b

print(end='\n')
print(end='\n')
print(end='\n')

#printing the value ,datatype and id of the variables
print(f'Name: {a}, type: {type(a)}, memory address: {id(a)}')
print(f'Age: {b}, type: {type(b)}, memory address: {id(b)}')
print(f'Height: {c}, type: {type(c)}, memory address: {id(c)}')
print(f'Fav_number: {d}, type: {type(d)}, memory address: {id(d)}')
print(f'current_year: {e}, type: {type(e)}, memory address: {id(e)}')

print(end='\n')
print(end='\n')
print(end='\n')

#printing the summary of the user information
print(f'''Your name is '{a}'! ,
You are '{b}' years old,
Your height is '{c}',
Your favorite number is'{d}',
and your birth year is '{f}' according to your age '{b}'!''')

print(end='\n')
print(end='\n')
print(end='\n')

#Thanking at the last
print('Thank you for using interactive personal data collector, hope you liked it')
print('    __________                                                     ___             ')
print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 