givenString = input('Enter string list with comma: ')


def check_first_last_character(given_string):
    split_numbers = given_string.split(',')
    answer = 0
    for word in split_numbers:
        if word[0] == word[-1]:
            answer += 1
    return answer


print(check_first_last_character(givenString))