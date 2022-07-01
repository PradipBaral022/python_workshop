#LIST


my_list=['Pradip',22,80]
another_list =['Chomu']
print(my_list+another_list)
print(my_list[0]) #indexing
print(len(my_list))
print('This is slicing down')
print(my_list[1:]) #slicing
print('This is reversing down')
print(my_list[::1])
#unlike the string we can change the element inside the list
#as in the string we could not change the element inside 
print('This is new list after appending')
my_list[0]='Pradeep'
print(my_list)
#to append the new item/element in the list we can use the inbuilt function append()
my_list.append('Hero')
print(my_list)
popped_item=my_list.pop()
print(popped_item)
print(my_list)
my_list.pop(1)
print(my_list)

#sorting
the_list=[1,5,7,2,3,9]
string_list=['a','j','b','z']
the_list.sort()
string_list.sort()
print(string_list)
print(the_list)

#Reversing the list
the_list.reverse()
print(the_list)
the_list.reverse()
print(the_list)

the_list=[0]*3
print(the_list)

#nested list
a_list =[1,2,[3,"Pradip"]]
print(a_list[2][1])
a_list[2][1]="Chomu"
print(a_list)