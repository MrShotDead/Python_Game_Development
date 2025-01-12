sample_dict = {"name"  :  "Arindam", "age"   :  32, "city"  :  "Bangalore"}
# {keys : values}
# We are going to use the key in order to access the value, but vice-versa case is not possible
print(sample_dict["age"])
print(sample_dict)

sample_list = ["Arindam", 32, "Bangalore"]
print(sample_list)

print(sample_list[0])
print(sample_list[-1])
print("\n")
print(sample_dict.keys())
print(sample_dict.values())

#Adding items in a dictionary
sample_dict["Profession"] = "Engineer"
print(sample_dict)

# Deleting items from a dictionary
del sample_dict["Profession"]
print("\n")
print(sample_dict)

# Modify/Update value in a dictionary
sample_dict["age"] = 31
print(sample_dict)
print("\n")
print(sample_dict.items())

# Create a nested dictionary
classroom = {
  "Arindam":{
    "age" : 32,
    "marks" : [91, 88, 94, 93, 87]
  },
  "Sudhanva":{
    "age" : 11,
    "marks" : [96, 91, 93, 88, 92]
  }
}
print("\n")
print(classroom.keys())
print(classroom.values())
print("\n")

print(classroom.items())
