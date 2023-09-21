message_count_n = int(input())

for _ in range(message_count_n):
    actual_message_n = int(input())
    if actual_message_n == 88:
        print("Hello")
    elif actual_message_n == 86:
        print("How are you?")
    elif not actual_message_n == 88 and not actual_message_n == 86 and actual_message_n <= 88:
        print("GREAT!")
    elif actual_message_n > 88:
        print("Bye.")
