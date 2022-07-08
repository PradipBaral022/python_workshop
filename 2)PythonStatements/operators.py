#this is for the useful operators used in python
#Range()
print("Lets go through the built in function of python i.e Range()")
print("This will print all the values starting from 0 to less than 10 i.e upto 9")
for x in range(10):
    print(x)
print("This will print from 1 to 5 with step 4 ie it only print 1 and 3")
for idx in range(1,5,2):
    print(idx)
    #first is the starting, second is the ending but not including and last one is for the step
print("we can also print the list using this funciton as:")
print(list(range(13,20)))

#Enmumerate function
#insted of doing this we can use built in function enumerate
print("Without using enumerate function:")
cnt=0
for x in 'abcde':
    print(f'The index value of {x} is {cnt}')
    cnt+=1
print('With using enumerate function:')
print("Now lets go through the enumerate function in python")
count=0
words="abcde"
for x in enumerate('abcde'):
    print(x)
for x,y in enumerate(words):
    print(x)
    print(y)
    print('\n')
    #as tuple unpacking is the property of the tuples so we can also use that here as above code

#Zip() function
mylist1=[1,2,3]
mylist2=["Pradip","Dai","Programmer"]

print(zip(mylist1,mylist2))
for item in zip(mylist1,mylist2):
    print(item)
for item1,item2 in zip(mylist1,mylist2):
    print(item1)
    print(item2)
    print('\n')

#in operator
#this is used to check the elements in the list,dictionary and tuple
print('Now lets go through the in operator in python:')
print('x' in [1,2,3])
print('x' in ['x','y'])
print("For dictionary")
dc={'k1':123,'k2':'bc'}
print('k3' in dc.keys())
print('k2' in dc)
print(123 in dc) #this won't work as we have to specify the dc.values and it is better to code dc.keys() for the keys although we need not to write dc.keys for the keys
print(123 in dc.values())

#min max function
print("Use of min and max functions in python")
lst=[1,300,999,500,0]
print(max(lst))
print(min(lst))

#random library
print("Now lets use the random function in python")
from random import shuffle
#it randomly suffles around any sort of list
lst1=[1,2,3,4,5,6,7,8,9]
shuffle(lst1)
print(lst1)
print(type(shuffle(lst1)))

from random import randint
print(randint(0,150))

#input function
st=input('Enter your name:')
print(f'Welcome {st}')