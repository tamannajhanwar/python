print('hello and welcome to Employee management system')

while True:
    print('choose an option:')
    print('1.Create an employee')
    print('2.Create a manager')
    print('3.Create a developer')
    print('4.Show details')
    print('5.Exit')
    a=int(input('Enter ypur choice: '))
    
    #creating an employee
    if a==1:
        class Employee:
            def __init__(self):
                self.name=None
                self.age=None
                self.id=None
                self.salary=None

            def setdata(self):
                self.name=input('enter name: ')
                self.age=int(input('Enter age: '))
                self.id=input('Enter id: ')
                self.salary=int(input('Enter salary: '))

            def getdata(self):
                print(f'''employee create with
                name: {self.name}
                age: {self.age}
                id: {self.id}
                salary: {self.salary}''')
        emp=[]
        n=int(input('how many employee you want to create: '))
        for i in range(n):
            emp.append(Employee())
        for i in range(n):
            emp[i].setdata()
        for i in range(n):
            emp[i].getdata()
    
    # creating a manager
    elif a==2:
        class Manager(Employee):
            def __init__(self):
                super().__init__()
                self.department=None

            def setdata(self):
                super().setdata()
                self.department=input('enter the department: ')

            def getdata(self):
                print(f'''manager create with
                name: {self.name}
                age: {self.age}
                id: {self.id}
                salary: {self.salary}
                department: {self.department}''')
        man=[]
        n=int(input('how many manager you want to create: '))
        for i in range(n):
            man.append(Manager())
        for i in range(n):
            man[i].setdata()
        for i in range(n):
            man[i].getdata()

    elif a==3:
        class Developer(Employee):
            def __init__(self):
                super().__init__()
                self.programing_lang=None

            def setdata(self):
                super().setdata()
                self.programing_lang=input('Enter the programing language: ')

            def getdata(self):
                print(f'''developer create with
                name: {self.name}
                age: {self.age}
                id: {self.id}
                salary: {self.salary}
                programing_lang: {self.programing_lang}''')
        devl=[]
        n=int(input('how many developer you want to create: '))
        for i in range(n):
            devl.append(Developer())
        for i in range(n):
            devl[i].setdata()
        for i in range(n):
            devl[i].getdata()

    elif a==4:
        print('choose detais to show')
        print('1.employee')
        print('2.manager')
        print('3.developer')
        b=int(input('Enter the choice: '))

        if b==1:
            print('employee details:')
            for e in emp:
               e.getdata() 
        elif b==2:
            print('manager details:')
            for e in man:
                e.getdata()
        elif b==3:
            print('develper details:')
            for e in devl:
                e.getdata()
        else:
            print('invalid choice')
    elif a==5:
        print('Thank you for using Employee management system , hope you liked it')
        print('    __________                                                     ___             ')
        print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
        print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
        print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
        print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
        break