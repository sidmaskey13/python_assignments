givenString = input('Enter string: ')


def extract_join(given_string):
    if len(given_string) >= 2:
        first = given_string[:2]
        last = given_string[-2:]
        answer = first + last
    else:
        answer = ""
    return answer


print(extract_join(givenString))
