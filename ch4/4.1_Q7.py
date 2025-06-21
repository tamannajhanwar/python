#Q7

def names(*n):
    if not n:
        print('the list is empty')
    else:
        for i in n:
            print(i)
names('tamanna','bhumi','aarti')