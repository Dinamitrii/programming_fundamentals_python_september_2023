people_count = int(input())
elevator_capacity = int(input())

full_elevator_courses = people_count // elevator_capacity

extra_people = people_count % elevator_capacity

if extra_people > 0:
    full_elevator_courses += 1
else:
    full_elevator_courses = full_elevator_courses

print(full_elevator_courses)
