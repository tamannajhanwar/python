import datetime as dt 
import time
import math 
import maths 
import random 
import uuid
print('======================================')
print('  Welcome to multi-utility toolkit')
print('======================================')

while True:
    print('choose an option')
    print('1.Datetime and Time operation')
    print('2.Mathematical operation')
    print('3.Random Data Generation')
    print('4.Generate Unique Identifiers(UUID)')
    print('5.File operation (custom module)')
    print('6.Explore module attributes(dir())')
    print('7.Exit')
    print('======================================')
    a=int(input('enter your choice: '))

    if a==1:
        print('Datetime and Time operations:')
        print('1.Display current date and time')
        print('2.Calculate difference between two dates/times')
        print('3.Format date into custom format')
        print('4.Stopwatch')
        print('5.Countdown timer')
        print('6.Back to main menu')
        print('======================================')
        while True:
            c=int(input('Enter your choice: '))
            
            if c==1:
                print('Current Date and Time: ',dt.datetime.now())
                print('======================================')
            elif c==2:
                dtformat='%Y-%m-%d %H-%M-%S'
                f_dt=input('enter first date(year-month-date hour-min-sec): ')
                s_dt=input('enter second date(year-month-date hour-min-sec): ')
                try:
                    f_date=dt.datetime.strptime(f_dt,dtformat)
                    s_date=dt.datetime.strptime(s_dt,dtformat)
                    difference=s_date-f_date
                    print('difference',difference)
                    print('======================================')
                except:
                    print('entered date nd time is not in the "year-month-date hour-min-sec" format')
                    print('======================================')
            elif c==3:
                now=dt.datetime.now()
                print('format time: ',now)
                print('custom date: ',now.strftime("%d-%m-%Y %S-%M-%H"))
                print('======================================')
            elif c==4:
                input('press enter to start')
                start=time.time()
                input('press enter to stop')
                end=time.time()
                print(f'time stoped in {end-start} seconds')
                print('======================================')
            elif c==5:
                try:
                    seconds=int(input('enter the seconds of countdown: '))
                    for i in range(seconds,0,-1):
                        print(i,end='\r')
                        time.sleep(1)
                    print('Times up!!')
                    print('======================================')
                except:
                    print('seconds enteres is not in integer')
                    print('======================================')
            elif c==6:
                break
            else:
                print('enter the choice in integer from 1 to 6')
                print('======================================')
    elif a==2:
        while True:
            print('mathematical operation:')
            print('1. Calculate factorial')
            print('2. Solve compound interest')
            print('3. Trignometric calculations')
            print('4. Area of geometric shapes')
            print('5. Back to main menu')
            print('======================================')
            m=int(input('Enter your choice: '))
            
            if m==1:
                f=int(input('Enter the number: '))
                print('Factorial is',math.factorial(f))
                print('======================================')
            elif m==2:
                print(maths.compound_int())
                print('======================================')
            elif m==3:
                print('choose an option:')
                print('1.sin')
                print('2.cos')
                print('3.tan')
                print('4.back to math opertion menu')
                print('======================================')
                while True:
                    t=int(input('Enter your choice: '))

                    if t==1:
                        d=float(input('enetr the degree: '))
                        ead=math.radians(d)
                        print(f'sin {d} = {math.sin(ead)}')
                        print('======================================')
                    elif t==2:
                        d=float(input('enetr the degree: '))
                        ead=math.radians(d)
                        print(f'cos {d} = {math.cos(ead)}')
                        print('======================================')
                    elif t==3:
                        d=float(input('enetr the degree: '))
                        ead=math.radians(d)
                        print(f'tan {d} = {math.tan(ead)}')
                        print('======================================')
                    elif t==4:
                        break
                    else:
                        print('enter your choice in integer from 1 to 4')
                        print('======================================')
            elif m==4:
                print('choose an option')
                print('1.area of triangle')
                print('2.area of square')
                print('3.area of ractangle')
                print('4.area of circle')
                print('5.back to math operation menu')
                print('======================================')
                while True:
                    b=int(input('Enter your choice: '))
                    if b==1:
                        print(maths.area_t())
                        print('======================================')
                    elif b==2:
                        print(maths.area_s())
                        print('======================================')
                    elif b==3:
                        print(maths.area_r())
                        print('======================================')
                    elif b==4:
                        print(maths.area_c())
                        print('======================================')
                    elif b==5:
                        break
                    else:
                        print('enter your choice in integer from 1 to 5')
                        print('======================================')
            elif m==5:
                break
            else:
                print('Enter your choice in integer from 1 to 5')
                print('======================================')
    elif a==3:
        print('Random Data eneration:')
        print('1.Generate random number')
        print('2.Generate random list')
        print('3.create random password')
        print('4.Generate random OTP')
        print('5.Back to main menu')
        print('======================================')
        while True:
            r=int(input('Enter your choice: '))

            if r==1:
                try:
                    print('Enter the two numbers between which you want random numbers')
                    n=int(input('enter the first number: '))
                    n1=int(input('enter the last number: '))
                    print('random number is: ',random.randint(n,n1))
                    print('======================================')
                except ValueError:
                    print('Enter the value in integer')
                    print('======================================')
            elif r==2:
                try:
                    g=input('Enter the list of numbers seperated by comma: ')  
                    j=[int(i) for i in g.split(',')]  
                    h=int(input('Enter how many random numbers you want in your list: '))   
                    print('random list is: ',random.choices(j,k=h))
                    print('======================================')
                except ValueError:
                    print('Enter the numbers in integer')
                    print('======================================')
            elif r==3:
                try:
                    e=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                    o=['!','@','#','%','^','&','*','/','_','|']
                    p=['1','2','3','4','5','6','7','8','9','0']
                    z=e+l+o+p
                    u=int(input('Enter the length of your password: ')) 
                    print('random password is: ',''.join(random.choices(z,k=u)))
                    print('======================================')
                except ValueError:
                    print('Enter the numbers in integer')
                    print('======================================')
            elif r==4:
                try:
                    q=['1','2','3','4','5','6','7','8','9','0']
                    s=int(input('Enter the length of your OTP: ')) 
                    print('random OTP is: ',''.join(random.choices(q,k=s)))
                    print('======================================')
                except:
                    print('Enter the numbers in integer')
                    print('======================================')
            elif r==5:
                break
            else:
                print('Enter your choice in integer from 1 to 5')
                print('======================================')
    elif a==4:
        print('uuid operation: ')
        print('1.generate unique id')
        print('2.back to main menu')
        while True:
            v=int(input('enter your choice: '))
            
            if v==1:
                print('generated uuid: ',uuid.uuid4())
                print('======================================')
            elif v==2:
                break
            else:
                print('Enter your choice in integer from 1 to 2')
                print('======================================')
    elif a==5:
        print('file operation:')
        print('1.create a new file')
        print('2.write to a file')
        print('3.read from a file')
        print('4.append to a file')
        print('5.back to main menu')
        while True:
            w=int(input('enter your choice: '))

            if w==1:
                try:
                    x=input('enter the file name: ')
                    y=open(f'C:\\Users\\Admin\\Desktop\\{x}.txt',"x")
                    y.close()
                    print('file created successfully!')
                    print('======================================')
                except:
                    print('file already exists')
                    print('======================================')
            elif w==2:
                try:
                    z=input('Enter the file name: ')
                    w_y=open(f'C:\\Users\\Admin\\Desktop\\{z}.txt',"r+")
                    write=input('enter the data: ')
                    w_y.write(write)
                    w_y.close()
                    print('Data entered successfully!')
                    print('======================================')
                except:
                    print('file not found!')
                    print('======================================')
            elif w==3:
                try:
                    read_f=input('Enter the file name: ')
                    read_y=open(f'C:\\Users\\Admin\\Desktop\\{read_f}.txt',"r")
                    print('file content is:\n',read_y.read())
                    read_y.close()
                    print('======================================')
                except:
                    print('file not found!')
                    print('======================================')
            elif w==4:
                try:
                    append=input('enter the file name: ')
                    a_f=open(f'C:\\Users\\Admin\\Desktop\\{append}.txt','a')
                    a_write=input('enter the data: ')
                    a_f.write(a_write)
                    a_f.close()
                    print('======================================')
                except:
                    print('file not found!')
                    print('======================================')
            elif w==5:
                break
            else:
                print('enter your choice in integer between 1 to 5')
                print('======================================')
    elif a==6:
        print('module attributes:')
        print('1.explore module')
        print('2.back to main menu')
        while True:
            ma=int(input('Enter your choice: '))

            if ma==1:
                try:
                    xm=input('Enter module name to explore: ')
                    mod=__import__(xm)
                    print('available attributes in ',mod,'module: \n',dir(mod))
                    print('======================================')
                except:
                    print('module not exists!')
                    print('======================================')
            elif ma==2:
                break
            else:
                print('enter your choice in integer from 1 to 2')
                print('======================================')
    elif a==7:
        print('======================================')
        print('Thank you for using the multi utility toolkit!')
        print('======================================')
        print('    __________                                                     ___             ')
        print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
        print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
        print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
        print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
        break
    else:
        print('enter your choice in integer from 1 to 7')
        print('======================================')