givenString = input('Enter string: ')


def check_upper_lower_letters(given_string):
    lower_count = 0
    upper_count = 0
    for char in given_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return f"""
    Number of upper case characters: {upper_count}
    Number of lower case characters: {lower_count}
    """


print(check_upper_lower_letters(givenString))