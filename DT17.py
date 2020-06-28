givenString = input('Enter number list with comma: ')


def multiple_list_numbers(given_string):
    answer=1
    split_numbers = given_string.split(',')
    for number in split_numbers:
        answer *= int(number)
    return answer


print(multiple_list_numbers(givenString))