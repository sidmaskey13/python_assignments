givenString = input('Enter number list with comma: ')


def smallest_number(given_string):
    split_numbers = given_string.split(',')
    smallest = int(split_numbers[0])
    for number in split_numbers:
        if smallest > int(number):
            smallest = int(number)
    return smallest


print(smallest_number(givenString))