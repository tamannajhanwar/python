#Q9

#converting list into set and tuple
a=input('Enter the list: ')
b=[i for i in a.split()]
print('the list is',b)
c=set(b)
print('the converted list into set is',c)
d=tuple(b)
print('the converted list into tuple is',d)

#converting tuple into a list
t=input('Enter the tuple: ')
e=[j for j in t.split()]
print('the tuple is',e)
l=list(e)
print('The converted tuple into list is',l )

#converting a set into list and tuple
s=set(input('Enter the set: '))
print('The set is',s)
g=list(s)
print('The converted set into list is',g)
h=tuple(s)
print('the converted set into tuple is',h)