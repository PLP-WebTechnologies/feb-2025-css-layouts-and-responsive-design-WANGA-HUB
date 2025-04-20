my_list = []
print("Before Append: ", my_list)
my_list.append(10)
print("After Append: ", my_list)
my_list.append(20)
print("After Append: ", my_list)
my_list.append(30)
print("After Append: ", my_list)
my_list.append(40)
print("After Append: ", my_list)

my_list.insert(2, 15)
print("After Insertion: ", my_list)

new_list = [50, 60, 70]
my_list.extend(new_list)
print("After Extend: ", my_list)

del my_list[-1]
print("After Deletion: ", my_list)

sorted_list = sorted(my_list)
print("Sorted List: ", sorted_list)

print(my_list[-4])