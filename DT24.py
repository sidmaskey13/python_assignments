from copy import deepcopy

givenList = input('Enter list: ')


def copy_list(given_string):
    new_list = []
    new_list = deepcopy(given_string)
    return new_list


print(copy_list(givenList))