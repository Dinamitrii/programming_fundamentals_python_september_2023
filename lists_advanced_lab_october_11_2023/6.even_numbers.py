numbers_list = list(map(int, input().split(", ")))

found_indexes_or_no = map(lambda x: x if numbers_list[x] % 2 == 0 else "no", range(len(numbers_list)))

even_indexes = list(filter(lambda a: a != "no", found_indexes_or_no))

print(even_indexes)
