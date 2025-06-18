#welcome
print('hello and welcome to the data analyzer and transformer program')
print(end="\n")
print(end="\n")
#main menu
print('1.Input data')
print('2.Display data summary(Built in fuction)')
print('3.Calculate factorial(recursion)')
print('4.Filter data by lambda function')
print('5.Sort data')
print('6.Dispaly dataset statistics(return multiple values)')
print('7.Exit program')

print(end="\n")
print(end="\n")

data=[]

while True:
    choice=int(input("Enter your choice: "))
    print(end="\n")
    if choice==1:
        data_input=input('Enter data for a 1D array (seperated by spaces):')
        data=list(map(int,data_input.split()))
        print('Data has been stored successfully!')
        print(end="\n")
        print(end="\n")
    elif choice==2:
        print('data summary')
        print('total elements: ',len(data))
        print('maximum value: ',max(data))
        print('minimum value: ',min(data))
        print('sum of all values: ',sum(data))
        print('average value: ',sum(data)/len(data))
        print(end="\n")
        print(end="\n")
    elif choice==3:
        def fact(n):
            f=1
            for i in range(1,n+1):
                f=f*i
            print(f)
        ft=int(input('Enter the number to calculate factorial: '))
        print(fact(ft))
        print(end="\n")
        print(end="\n")
    elif choice==4:
        filt=int(input('enter a value to filter out data above this value: '))
        f=list(filter(lambda x:x >= filt,data))
        print('filtered data: ',f)
        print(end="\n")
        print(end="\n")
    elif choice==5:
        print('choose sorting option:')
        print('1.ascending')
        print('2.descending')
        a=int(input('enter your choice: '))
        print(end="\n")
        if a==1:
            print('sorted data in ascending is',sorted(data))
            print(end="\n")
            print(end="\n")
        elif a==2:
            print('sorted data in descending is',sorted(data,reverse=True))
            print(end="\n")
            print(end="\n")
    elif choice==6:
        print('dataset statistics')
        print('maximum value: ',max(data))
        print('minimum value: ',min(data))
        print('sum of all values: ',sum(data))
        print('average value: ',sum(data)/len(data))
        print(end="\n")
        print(end="\n")
    elif choice==7:
        #thank you note
        print('Thank you for using data analyzer and transformer pr0gram , hope you liked it')
        print('    __________                                                     ___             ')
        print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
        print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
        print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
        print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
        break