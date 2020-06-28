givenString = input('Enter string: ')


def change_word(given_string):
    answer = ""
    if len(given_string) > 3:
        if given_string[-3:] == "ing":
            answer = given_string+"ly"
        else:
            answer = given_string+"ing"
    else:
        answer = given_string
    return answer


print(change_word(givenString))


