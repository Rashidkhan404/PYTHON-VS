#  its all about intersection in set
set1 = {'arif', 'Rashid', 'shyam', 'jenny'}
set2 = {'Mohsin', 'rahman', 'sud..', 'myk', 'Rashid'}
set3 = {'pajee', 'baloch', 'Dewana'}
print(set1.intersection(set2))
print(set2.intersection(set1))
#  print(set1 & set2) intersection by operator
# for upadate the intersection
set1.intersection_update(set2)
# set2.intersection_update(set1)
# we can pass as argument List, Tuple, Dictionary
# it will give the empty set because thereis no common
set2.intersection_update(['shahab', 'ali'])
print(set2)
print(set1)
