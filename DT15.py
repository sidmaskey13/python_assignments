givenTagString = input('Enter tag string: ')
givenString = input('Enter string: ')


def insert_string_in_middle(given_tag_string, given_string):
    tag_string_length=len(given_tag_string)
    return f"""{given_tag_string[:int((tag_string_length/2)-1)]}{given_string}{given_tag_string[int(-tag_string_length/2):]}"""


print(insert_string_in_middle(givenTagString, givenString))