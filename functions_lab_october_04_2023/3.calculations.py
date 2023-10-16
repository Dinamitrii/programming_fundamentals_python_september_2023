operator = input()
first_num = int(input())
second_num = int(input())


def solve_function(x, y, operator):
    result = None
    if operator == "multiply":
        result = x * y
    elif operator == "divide":
        result = int(x / y)
    elif operator == "add":
        result = x + y
    elif operator == "subtract":
        result = x - y
    return result


print(solve_function(first_num, second_num, operator))
