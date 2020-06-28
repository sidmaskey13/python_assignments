givenString = input('Enter number list with comma: ')


def largest_number(given_string):
    split_numbers = given_string.split(',')
    largest = int(split_numbers[0])
    for number in split_numbers:
        if largest < int(number):
            largest = int(number)
    return largest


print(largest_number(givenString))