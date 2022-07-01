#formatting with the .format() method
#'Strings here {} then also {}'.format('smt1','smt2')
#this is mainly for string concatenations
print('This is string {}'.format('It is not the number'))

#float formatting follows as:"{value:width.percisoin f}"
result= 700.890939393
#to copy the code on next line the shortcut is option shift and down
print("The result was {r:10.2f}".format(r=result))
print("The result was {r:1.2f}".format(r=result))

#f strings or strings literals
names = "Pradip"
print(F"Hi, I am {names}")
name='Pradip'
a=F'The name is {name}'
print(a)
print(F'The name of the hero is {name}')
