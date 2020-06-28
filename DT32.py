givenNumber = int(input('Enter number: '))


def square_dictionary(given_number):
    dictionary = dict()
    for i in range(1, given_number+1):
        key, value = i, i*i
        new_data = {key: value}
        dictionary.update(new_data)
    return dictionary


print(square_dictionary(givenNumber))