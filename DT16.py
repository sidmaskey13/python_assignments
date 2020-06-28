givenString = input('Enter number list with comma: ')


def sum_list_numbers(given_string):
    sum=0
    split_numbers = given_string.split(',')
    for number in split_numbers:
        sum += int(number)
    return sum


print(sum_list_numbers(givenString))