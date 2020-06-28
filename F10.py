givenList = input('Enter number List: ')


def only_even_list(given_string):
    no_brackets = given_string.replace(" ", "").strip("[]").strip("()")
    strip_list = no_brackets.split(",")
    answer = [i for i in strip_list if int(i) % 2 == 0]
    return answer


print(only_even_list(givenList))