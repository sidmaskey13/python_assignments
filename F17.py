givenString = input('Enter string: ')
givenCharacter = input('Enter character: ')


def check_character_string(given_string, given_character):
    answer = lambda x: x == given_string[0]
    if answer(given_character):
        return f"{given_character} is first character in {given_string}"
    else:
        return f"{given_character} is not first character in {given_string}"


print(check_character_string(givenString, givenCharacter))