# List
my_list = [30, 10, 20, 40]
print("Original List:", my_list)
my_list.append(50)
my_list.insert(1, 15)
my_list.remove(40)
my_list.sort()
my_list.pop()
print("Modified List:", my_list)

# Tuple
my_tuple = (10, 20, 20, 30, 40)
print("\nOriginal Tuple:", my_tuple)
print("Occurrences of 20:", my_tuple.count(20))
print("Position of 30:", my_tuple.index(30))
print("Specified portion:", my_tuple[1:4])
another_tuple = (50, 60)
combined_tuple = my_tuple + another_tuple
print("Combined Tuple:", combined_tuple)
print("Element at position 2:", my_tuple[2])

# Dictionary
my_dict = {"Name": "Rahul", "Age": 18, "Course": "Computer Engineering"}
print("\nOriginal Dictionary:", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Key-Value Pairs:", my_dict.items())
my_dict["Age"] = 19
my_dict["City"] = "Pune"
my_dict.pop("Course")
print("Modified Dictionary:", my_dict)