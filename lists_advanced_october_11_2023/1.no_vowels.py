user_text_input = input()

sorted_text = [char for char in user_text_input if char.lower() not in ["a", "o", "u", "e", "i"]]

print("".join(sorted_text))
