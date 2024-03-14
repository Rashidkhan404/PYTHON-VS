# set in python
# set is a orderless(elements have no defined order)
# indexes are not allowed
# we can add or remove the elements
# slicing is not allowed
# duplicate element are not allowed
# we can add tuple
# we cant add List beacuse List are mutable
set1 = {10, 56, 89, 99, 'jenny', True, 1}
set1.add(99)
set1.remove(99)
set1.discard(68)
print(set1.pop())
set1.add((23, 24, 25))  # we can add tuple
#  set1.clear()
set2 = set()  # empty set
print(type(set2))
print(set1)
print(len(set1))
