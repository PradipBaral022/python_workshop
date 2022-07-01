#Notes on dictionaries on python

my_dict={1: 'value1',
         'key2': 'value2'
}
print(my_dict[1])
print(my_dict['key2'])

#inside the dictionary we can add list and even another dictionary
d={
    'key1':123,
    2:[1,2,3],
    3.333:['Pradip','chomu'],
    'dict':{4:'Pradip dai'}
}
print(d['key1'])
print(d[2])
print(d[3.333])
print(d['dict'][4])
print(d[3.333][1]) #indexing inside the list

#here also in dictionaries like of the list we can append or add new key and value

d['addedKey'] = 'Added'
print(d)

#to know the keys
print(d.keys())


#to find the values
print(d.values())

#to print the pairs of keys and items
print(d.items())


#here we are using key as any data types but it is better practise to use strings as the key
