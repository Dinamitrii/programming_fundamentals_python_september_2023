def min_max_sum():
    list_of_integers = list(map(int, integer_input_as_string))

    minimum = min(list(list_of_integers))
    maximum = max(list(list_of_integers))
    sum_numbers = sum(list(list_of_integers))
    return print(f"The minimum number is {minimum}\nThe maximum number is {maximum}\nThe sum number is: {sum_numbers}")


integer_input_as_string = input().split()


min_max_sum()
