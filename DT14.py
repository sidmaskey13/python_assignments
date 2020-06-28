givenTag = input('Enter tag: ')
givenString = input('Enter string: ')


def add_tag_around_word(given_tag, given_string):
    return f"""<{given_tag}>{given_string}<{given_tag}>"""


print(add_tag_around_word(givenTag, givenString))