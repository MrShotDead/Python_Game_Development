address = ("P901", "Supertech Ecociti", "Noida Sector 137", 201301)
# 1. Tuples are always enclosed in round brackets
# 2. Tuples can be unpacked
# 3. Tuples also have similar indexing concepts just like Lists




AptNum, AptName, Area, ZipCode = address

print("\nMy apartment number is", AptNum)
print("My Apartment Name is", AptName)
 #The above concept is known as unpacking, where we 
 #can unpack values of Tuple into separate variables

abc = ("Sudhanva", 123, 12.87, True, [7, 77, 777, "Hello Sudhanva"], (12, 24, 36))
print(type(abc))

print("\n")
print(abc[1])
print(abc[4][3][10])

print(abc[1:4]) 

xyz = ("Hello", 78941236, 147.968, False, ["List", 123, 14.79], ("World", 369, 14.12))
print(xyz[0:2])

print(xyz[3:30])

print("\n")
print(xyz[:4])
print(xyz[2:])

print(xyz[:])




