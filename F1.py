firstNumber = int(input('Enter 1st number: '))
secondNumber = int(input('Enter 2nd number: '))
thirdNumber = int(input('Enter 3rd number: '))


def largest_among_three(first_number, second_number, third_number):
    new_list = [first_number, second_number, third_number]
    return f"largest is {max(new_list)}"


print(largest_among_three(firstNumber, secondNumber, thirdNumber))

