givenString = input('Enter string: ')


def remove_odd_index(given_string):
    return given_string[1::2]


print(remove_odd_index(givenString))