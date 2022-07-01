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

for _ in 'Hello world':
    print(_)

