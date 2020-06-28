dictionary = {'a': 2, 'b': 3, 'c': 5, 'd': 6}
answer = 1
for key, value in dictionary.items():
    answer *= value
print(f"Multiply of dictionary values are {answer}")
