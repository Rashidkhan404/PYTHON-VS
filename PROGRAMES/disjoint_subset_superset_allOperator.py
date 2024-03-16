
# desjoint(no operator),subset(<=),superset(>=),union(|),intersection(&)
# difference(-), symmatric_difference(^)
set1 = {'Ram', 'shyam', 'jenny'}
set2 = {'jiya', 'karish'}
print(set1.isdisjoint(set2))  # true beacuse there is no common element
print(set1.isdisjoint(['Mohan', 'kali']))
# for subset every element of set1 is present in set2
print(set1.issubset(set2))
print(set1.issubset(['Ram', 'shyam', 'jenny', 'mohan']))
# subset by operator
print(set1 <= set1)
# every element of set2 present in set1
print(set1.issuperset(set2))  # false beacuse evry element is not present
print(set1.issuperset(set1))  # true
# superset by operator
print(set1 >= set1)
set2.clear()  # it will clear all entries in set2
print(set2)
# del set2
# print(set2)
# the defference b/t clear and del is
# clear remove the entries but del remove the whole set
