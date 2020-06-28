givenString = input('Enter string: ')


def add_dollar_sign(given_string):
    answer = ""
    first_letter = given_string[0]
    for idx, item in enumerate(given_string):
        if idx == 0 or item != first_letter:
            answer = answer + item
        else:
            answer = answer + "$"
    return answer


print(add_dollar_sign(givenString))


