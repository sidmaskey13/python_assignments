dictionary = dict()
for i in range(1, 16):
    key, value = i, i * i
    new_data = {key: value}
    dictionary.update(new_data)
print(dictionary)