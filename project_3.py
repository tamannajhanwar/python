#description of the program
print('''Hello and welcome to student data organier!
This organizer helps to input the students details,
displaying all students records , updating information of students,
deleting a student information and displaying the unique subjects''')

print(end="\n")
print(end="\n")

#body of the code
student={}
while True:
    
    #printing options for user
    print('Enter 1 to add a student')
    print('Enter 2 to display all the students')
    print('Enter 3 to update the student information')
    print('Enter 4 to delete a student')
    print('Enter 5 to display all the unique subjects')
    print('Enter 6 to exit')
    a=int(input('Enter your choice: '))
    
    print(end="\n")
    print(end="\n")
    #add student
    if a==1:
        print("enter student details:")
        b=input('name: ')
        c=input('student ID: ')
        d=input('age: ')
        e=input('Grade: ')
        f=input('date of birth: ')
        g=input('subjects: ')
        student[c]={'name':b,'age':d,'grade':e,'subjects':g.split(',')}
        print(end="\n")
        print('student added successfully!')
        print(end="\n")
        print(end="\n")
    #display student
    elif a==2:
        if not student:
            print('no records found!')
        else:
            for i,j in student.items():
                print(f'student ID:{i} | Name:{j['name']} | Age:{j['age']} | Grade:{j['grade']} | subjects:{j['subjects']}')
        print(end="\n")
        print(end="\n")
    #update student
    elif a==3:
        id=input('Enter the student id: ')
        print(end="\n")
        if id in student:
            print("Enter 1 to update name ")
            print("Enter 2 to update age ")
            print("Enter 3 to update grade ")
            print("Enter 4 to update subject")
            print("Enter 5 to update everything ")
            c_2=int(input('enter your choice: '))
            print(end="\n")
            if c_2==1:
                student[id]['name']=input('name: ')
            elif c_2==2:
                student[id]['age']=input('age: ')
            elif c_2==3:
                student[id]['grade']=input('grade: ')
            elif c_2==4:
                student[id]['subjects']=input('subjects: '.split(','))
            elif c_2==5:
                student[id]['name']=input('name: ')
                student[id]['age']=input('age: ')
                student[id]['grade']=input('grade: ')
                student[id]['subjects']=input('subjects: '.split(','))
            else:
                print('invalid number')
                print(end="\n")
                print(end="\n")
        else:
            print('student id not found!')
            print(end="\n")
            print(end="\n")
    #delete student
    elif a==4:
        id_2=input('Enter student id: ')
        print(end="\n")
        if id_2 in student:
            del student[id_2]
            print('student deleted successfully!')
            print(end="\n")
            print(end="\n")
    #display subjects
    elif a==5:
        sub=[]
        for i in student:
            sub+=student[i]['subjects']
        print(set(sub))
        print(end="\n")
        print(end="\n")
    #exit
    elif a==6:
        #thank you note
        print('Thank you for using pattern generation and number analyer , hope you liked it')
        print('    __________                                                     ___             ')
        print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
        print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
        print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
        print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
        break