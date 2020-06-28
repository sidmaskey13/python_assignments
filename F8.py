givenString = input('Enter list: ')


def unique_list(given_string):
    no_brackets = given_string.replace(" ","").strip("[]").strip("()")
    strip_list = no_brackets.split(",")
    answer = []
    [answer.append(i) for i in strip_list if i not in answer]
    return answer


print(unique_list(givenString))