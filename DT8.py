givenString = input('Enter string: ')
indexNumber = input('Enter index number: ')


def delete_index_number(given_string, index_number):
    first = given_string[:int(index_number)]
    last = given_string[int(index_number)+1:]
    return first+last


print(delete_index_number(givenString, indexNumber))


