# symmatric difference in sets
set1 = {'Ram', 'Shyam', 'jenny'}
set2 = {'jenny', 'jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}
# we cannot pass many argument just like
# print(set1.symmatric_difference(set2,set3))
print(set1.symmetric_difference(set2))
# by operator it is apply for more sets
print(set1 ^ set2 ^ set3)
set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('Mohan', 'karish'))
print(set1)
