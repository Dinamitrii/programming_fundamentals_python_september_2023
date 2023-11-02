def coffee_lover():
    # Receive initial coffees list. Since coffees can be given over multiple lines, we concatenate them.
    coffees = []
    while True:
        line = input().strip()
        if line.isdigit():
            n = int(line)
            break
        coffees.extend(line.split())

    for _ in range(n):
        # Split the command into parts
        command_data = input().split()

        # Process the command "Include"
        if command_data[0] == "Include":
            coffee = command_data[1]
            coffees.append(coffee)

        # Process the command "Remove"
        elif command_data[0] == "Remove":
            if command_data[1] == "first":
                count = int(command_data[2])
                coffees = coffees[count:]
            elif command_data[1] == "last":
                count = int(command_data[2])
                coffees = coffees[:-count]

        # Process the command "Prefer"
        elif command_data[0] == "Prefer":
            index1 = int(command_data[1])
            index2 = int(command_data[2])

            # Ensure the indices are valid before swapping
            if 0 <= index1 < len(coffees) and 0 <= index2 < len(coffees):
                coffees[index1], coffees[index2] = coffees[index2], coffees[index1]

        # Process the command "Reverse"
        elif command_data[0] == "Reverse":
            coffees = coffees[::-1]

    # Display the final coffees list
    print("Coffees:")
    for coffee in coffees:
        print(coffee,end=" ")

coffee_lover()
