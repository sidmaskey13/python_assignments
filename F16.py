givenList = input('Enter list: ')


def square_cube_list(given_string):
    string_to_list = list(eval(given_string))
    squared_list = list(map(lambda x: x**2, string_to_list))
    cube_list = list(map(lambda x: x**3, string_to_list))
    return f"""
    Given list:{given_string}
    Squared list:{squared_list}
    Cube list:{cube_list}
    """


print(square_cube_list(givenList))