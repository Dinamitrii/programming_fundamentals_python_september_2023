def sort() -> list:
    list_of_integers = list(map(int, integer_input_as_string))

    return sorted(list_of_integers)


integer_input_as_string = input().split()

print(sort())
