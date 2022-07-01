#sets are the ordered collection of unique data
#meaning there can't be same number twice or more inside the set

my_set=set()
my_set.add(1)
print(my_set)
my_set.add(2)
my_set.add(1)
print(my_set)

#we can also pass/cast the list over the set to get only the unique values over the list as:
my_list = [2,2,2,2,3,3,3,3,4,4,4,4]
print(set(my_list))
