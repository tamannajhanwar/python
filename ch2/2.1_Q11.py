#Q11

for i in range(1,51):
    print(i)

    if i%2==0:
        print('divisable by 2')
    elif i%3==0:
        print('divisable by 3')
    elif i%2==0:
        if i%3==0:
            print('divisable by both')
    else:
        print('not divisable by 2 and 3')
