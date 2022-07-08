
mylist = [1,2,3,4]
for numbers in mylist:
    print(numbers)
# the particular variable name here i.e numbers can be anything according to the programmer

mylist = [1,2,3,4]
for numbers in mylist:
     print('hello world!')
#this will print four hello world!

print('Printing the odd numbers from the list')
for numbers in mylist:
    if numbers%2!=0:
        print(numbers)

print('Printting the sum of the squares:')
sum_squares=0
for numbers in mylist:
    sum_squares += numbers**2
print(sum_squares)

my_string="Pradip Baral"
for letters in my_string:
    print(letters)

#the variable name can be anything including any symbol i.e it is described by the user
for _ in 'Hello world':
    print(_)

#now let us learn about tuple unpacking from for loop
next_list=[(1,2),(3,4),(5,6)]
print(len(next_list))
for a,b in next_list:
    print(a)

#now lets discuss how to iterate to the dictionary through a foor loop
d={'k1':1,'k2':2,'k3':3}
print('If we try to print as like the tuples and list then only the key values will be printed as below')
for items in d:
    print(items)
print("So for printing key with value")

for a,b in d:
    print(a,b)
print("Printing only the values")
for a,b in d:
    print(b)
