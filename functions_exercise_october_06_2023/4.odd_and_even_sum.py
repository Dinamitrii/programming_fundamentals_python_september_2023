def odd_even_sums(some_numbers: str):
    sum_of_even = 0
    sum_of_odd = 0

    for digit in some_numbers:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_even, sum_of_odd


number = input()

sum_of_even_digits, sum_of_odd_digits = odd_even_sums(number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
