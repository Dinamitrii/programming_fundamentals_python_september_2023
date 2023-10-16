input_for_list_a = input().split(" ")
count_of_numbers_to_remove = int(input())

list_a = []

for reverting_to_int in input_for_list_a:
    list_a.append(int(reverting_to_int))

list_a.sort()
list_a.reverse()

for index in range(len(list_a)):
    print(index)
