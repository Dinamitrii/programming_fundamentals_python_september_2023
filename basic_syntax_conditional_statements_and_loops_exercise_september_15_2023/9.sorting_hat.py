gryffindor = []
slytherin = []
ravenclaw = []
hufflepuff = []

# Read student names until "Welcome!" or "Voldemort" is encountered
while True:
    name = input()

    if name == "Welcome!":
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        exit()

    name_length = len(name)

    if name_length < 5:
        gryffindor.append(name)
        print(f"{name} goes to Gryffindor.")
    elif name_length == 5:
        slytherin.append(name)
        print(f"{name} goes to Slytherin.")
    elif name_length == 6:
        ravenclaw.append(name)
        print(f"{name} goes to Ravenclaw.")
    else:
        hufflepuff.append(name)
        print(f"{name} goes to Hufflepuff.")

if "Voldemort" not in gryffindor + slytherin + ravenclaw + hufflepuff:
    print("Welcome to Hogwarts.")
