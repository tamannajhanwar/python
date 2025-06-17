#description of the program
print('''Hello and welcom to pattern generation and number analyzer!
It genertes pattern 
It analyse the numbers in odd and even and also gives the sum of numbers''')

print(end="\n")
print(end="\n")
print(end="\n")

#body of the code
while True:

    #printing the options for user
    print('Enter 1 in your choice to generate patterns ')
    print('Enter 2 in your choice to analyse number')
    print('Enter 3 in your choice to exit')
    a=int(input('enter your choice: '))

    print(end="\n")
    print(end="\n")
    print(end="\n")

    #pattern generator
    if a==1:
        print('"Enter a number one greater than the number of rows you want to print."')
        b=int(input('Enter the number of rows: '))
        for i in range(b):
            for j in range(1,i+1):
                print('@#',end=' ')
            print()

        print(end="\n")
        print(end="\n")
        print(end="\n")

    #number analyzer
    elif a==2:
        print('"The starting number must be greater than ending number"')
        c=int(input('Enter the starting number: '))
        d=int(input('Enter the ending number: '))
        for i in range(c,d+1):
            if i%2==0:
                print(f'{i} is an "even" number')
            elif i%2==1:
                print(f'{i} is a "odd" number')
        e=sum(range(c,d+1))
        print(end="\n")
        print(end="\n")
        print(f'Sum of all the numbers from {c} to {d} is',e)
    
        print(end="\n")
        print(end="\n")
        print(end="\n")

    #exit
    elif a==3:

        #thank you note
        print('Thank you for using pattern generation and number analyer , hope you liked it')
        print('    __________                                                     ___             ')
        print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
        print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
        print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
        print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
        break