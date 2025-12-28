#Sets are unorderd data types
#can't store duplicate values, only unic values only
# add() function use for adding a single values
# update() function use for add multiple values
# remove()/discard() function for remove values
  

  

my_list = ['kamal', 20, 'jaffna', False, 20]
my_tuple = ('kamal', 20, 'jaffna', False, 20)

my_set = {'kamal', 20, 'jaffna', False, 20}


print(type(my_set))
print(my_set)

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

print(A.intersection(B))
print(A.difference(B))



print(my_set)
my_set.add('nadun')
print(my_set)
my_set.update(['ranil', 'sajith'])
print(my_set)