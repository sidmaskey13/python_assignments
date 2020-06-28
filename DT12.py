givenString = input('Enter string: ')


def change_upper_lower(given_string):
    return f"""
    UpperCase: {given_string.upper()}
    LowerCase: {given_string.lower()}
    """


print(change_upper_lower(givenString))