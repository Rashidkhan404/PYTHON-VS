# set operation
# union in set
set1 = {"RASHID", "ARIF", "MOHSIN"}
set2 = {"MYK", "HUZI", "RAHMAN", "SUD"}
set3 = {"hello"}
print(set1 | set2)  # union of a 2 set
# or
print(set1.union(set2, set3))  # union of a set
# or
print(set2.union(set1))  # union of a set
# use of tuple
print(set1.union(("HI", "sorry")))
# but here tuple is not allowed
# print(set1 | ("HELLO", "HERE")) it gives error
# we can update the set
# set1.update(set2)
set1.update(["AQ", "sowad"])
print(set1)
