# difference in sets
set1 = {'Ram', 'Shyam', 'jenny'}
set2 = {'jenny', 'jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}
print(set1.difference(set2))
print(set1.difference(('Mohan', 'shiva')))
print(set1.difference(set2, set3))
set1.difference_update(set2)
print(set1)
print(set1 - set2)
