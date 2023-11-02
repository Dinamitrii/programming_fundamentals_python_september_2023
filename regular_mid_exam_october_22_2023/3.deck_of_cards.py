def process_commands(cards, commands):
    output = []
    for command in commands:
        parts = command.split(', ')
        if parts[0] == "Add":
            card = parts[1]
            if card in cards:
                output.append("Card is already in the deck")
            else:
                cards.append(card)
                output.append("Card successfully added")
        elif parts[0] == "Remove":
            card = parts[1]
            if card in cards:
                cards.remove(card)
                output.append("Card successfully removed")
            else:
                output.append("Card not found")
        elif parts[0] == "Remove At":
            index = int(parts[1])
            if 0 <= index < len(cards):
                del cards[index]
                output.append("Card successfully removed")
            else:
                output.append("Index out of range")
        elif parts[0] == "Insert":
            index = int(parts[1])
            card = parts[2]
            if 0 <= index <= len(cards):
                if card in cards:
                    output.append("Card is already in the deck")
                else:
                    cards.insert(index, card)
                    output.append("Card successfully added")
            else:
                output.append("Index out of range")
    return cards, output


# Example usage
initial_cards = input().split()
commands = input().split()

final_cards, messages = process_commands(initial_cards, commands)
print(', '.join(final_cards))
print(', '.join(messages))
