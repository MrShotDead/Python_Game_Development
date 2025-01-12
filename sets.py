#   *************** SETS *****************

# Sets are a collection of well defined objects. A unique property of set is that it does not store duplicate items
# Sets are always defined in curly braces


set1 = {1, 2, 3, 4, 5, 6, 4, 2}
print(set1)

xyz = [1, 3, 5, 7, 9, 3, 5]
print(xyz)

# Converting list to a set
sample_set = set(xyz)
print(sample_set)

# Check if an element exits in a set or not
if 9 in sample_set:
  print("\nYes it Exists!")
else:
  print("\nNo such item exists!")

# Create an empty set and do operations like adding, removing items from set

myset = set([])
# print(myset)

# Using the command add we can add items to the set
myset.add(21)
myset.add(38)
myset.add(-17)
myset.add(38)
myset.add(99)
print(myset)

# Using the command remove, we can remove/delete items from the set
myset.remove(-17)
print(myset)

# Remove command is most suited only when the item we want to remove is a aprt of the set, or else it throws an error

# myset.remove(108)
# print(myset)

# Discard does similar operations just like remove but it does not throw error for items which does not exist
print("\n")
myset.discard(21)
print(myset)
myset.discard(108)
print(myset)

# 1. Union --- All the items of both the sets, without repeating
# 2. Intersection --- Common items of both the sets
# 3. Difference --- (A - B), displays the item of set A by removing the common items with set B
# 4. Symmetric Difference --- Displays all the items of both the set, by excluding the common items only

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8, 10}

print(A | B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(B.difference(A))

print(A ^ B)
print(A.symmetric_difference(B))