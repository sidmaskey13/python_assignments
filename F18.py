givenString = input('Enter string: ')


def number_or_not(given_string):
    answer = lambda x: x.isnumeric()
    if answer(given_string):
        return f"{given_string} is number"
    else:
        return f"{given_string} is not number"


print(number_or_not(givenString))