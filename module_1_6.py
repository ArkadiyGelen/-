my_dict = {'Anton' : 2002, 'Max' : 2000}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Kamila'))
my_dict.update({'Alex' : 1999, 'Sahsa' : 1998})
a = my_dict.get('Anton')
del my_dict['Anton']
print(a)
print(my_dict)

my_set = [1, 4, 7, 2, 1, 3, 3, 7, 9, 'Max']
my_set = set(my_set)
print(my_set)
my_set.update([5, 8])
my_set.discard(1)
print(my_set)