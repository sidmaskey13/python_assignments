givenNumberX = int(input('Enter number X: '))
givenNumberY = int(input('Enter number Y: '))


def lambda_add_15(x,y):
    sum_x_15 = lambda a: a + 15
    multiply_x_y = lambda a, b: a * b

    return f"""
    Add 15: {sum_x_15(x)}
    Add X and Y: {multiply_x_y(x,y)}
    """


print(lambda_add_15(givenNumberX, givenNumberY))