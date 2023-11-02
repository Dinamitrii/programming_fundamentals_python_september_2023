def rounding_to_list():
    input_numbers = list(map(float, input().split()))
    round_to_whole = [round(num) for num in input_numbers]

    return round_to_whole


print(rounding_to_list())
