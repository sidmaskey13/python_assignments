given_tuple = (1,2,3,4,5,6)
print(f"Given Tuple: {given_tuple}")

temp_list = list(given_tuple)
to_remove = 3

print(f"To remove: {to_remove}")
temp_list.remove(to_remove)
new_tuple = tuple(temp_list)

print(f"New Tuple: {new_tuple}")
