"""Module Six Milestone: simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room.
current_room = "Great Hall"

print("Dragon Text Game")
print("Move with 'go north', 'go south', 'go east', or 'go west'.")
print("Type 'exit' to quit.")

# Gameplay loop: runs until the player types "exit".
while True:
    # 1. Display the current room.
    print(f"\nYou are in the {current_room}.")

    # 2. Prompt for a movement command or "exit".
    command = input("Enter your move: ").strip().lower()

    # 3. Branch for blank input, exit, a movement command, or invalid input.
    if not command:
        print("Please enter a command.")

    elif command == "exit":
        print("Thanks for playing.")
        break

    elif command == "go" or command.startswith("go "):
        direction = command[2:].strip()

        if not direction:
            print("Specify a direction, for example 'go south'.")
        elif direction in rooms[current_room]:
            # 4. Update the room only after a valid movement command.
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.")

    else:
        print("Invalid command. Use 'go [direction]' or 'exit'.")
