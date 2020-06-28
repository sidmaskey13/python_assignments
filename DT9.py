givenString = input('Enter string: ')


def exchange_first_last_character(given_string):
    return given_string[-1] + given_string[1:-2] + given_string[0]


print(exchange_first_last_character(givenString))


