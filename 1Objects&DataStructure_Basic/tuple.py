#tuples are similar like the list but they are immutable that is unchangable 
#once a element is assigned to the index position we can't reassigned the same index position here in tuple
#tuple use parenthesis i.e small bracket as:(1,2,3)

from audioop import mul
from xml.dom.minidom import TypeInfo


t = (1,2,3)
my_list=[1,2,3]
print(type(my_list))
print(type(t))
print(t)
print(my_list)
print(t[0])
#t[0]=5
#print(t)
#this is not supposed to be done here for tuple cuz unlike list we can't reassign the already indexed value
print(t[1:]) #this supports slicing and indexing too
print(t[-2])


#count or index in tuple
tu=('a','a','a','b')
print('The numbers of a in the tuple is:')
print(tu.count('a'))
print(tu.index('a')) #  this shows the index position of first a
print(tu.index('b'))