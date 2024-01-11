secret_message = input().split()

list_from_secret_message = ["".join(secret_message[::1])]

messages_list = list(list_from_secret_message)


print(chr(72))
print(messages_list)
# print(messages_list)
print(type(chr(60)))
