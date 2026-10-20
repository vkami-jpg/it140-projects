# Full Name: Kambela Mazoka
"""Project Two: Breach at the Lab, a text-based adventure game."""


def show_instructions():
    """Display the game objective and available commands."""
    print("Breach at the Lab")
    print("The Phantom is wiping evidence in the Halvorsen Digital Forensics Lab.")
    print("Collect all 6 items before you enter the Server Room.")
    print("Enter the Server Room too early and you lose.")
    print("\nCommands:")
    print("  go North, go South, go East, go West")
    print("  get [item name]")
    print("  exit")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\n" + "-" * 30)
    print(f"You are in the {current_room}.")
    print(f"Inventory: {', '.join(inventory) if inventory else 'empty'}")

    # Show the room's item only if the player has not collected it yet
    item = rooms[current_room]["item"]
    if item and item not in inventory:
        print(f"You see the {item}.")
    print("-" * 30)


def main():
    """Run the main gameplay loop."""
    # Room dictionary: each room maps directions to rooms and holds one item
    rooms = {
        "Lobby": {"North": "Server Room", "West": "Security Office", "item": None},
        "Security Office": {"East": "Lobby", "North": "Records Room",
                            "item": "Access Badge"},
        "Records Room": {"South": "Security Office", "North": "Break Room",
                         "item": "Network Log"},
        "Break Room": {"South": "Records Room", "East": "Forensics Lab",
                       "item": "Fingerprint Kit"},
        "Forensics Lab": {"West": "Break Room", "East": "Evidence Locker",
                          "item": "Encrypted Laptop"},
        "Evidence Locker": {"West": "Forensics Lab", "South": "Supply Closet",
                            "item": "Flash Drive"},
        "Supply Closet": {"North": "Evidence Locker", "West": "Server Room",
                          "item": "Decryption Key"},
        "Server Room": {"South": "Lobby", "East": "Supply Closet", "item": None},
    }
    valid_directions = ["North", "South", "East", "West"]
    total_items = 6

    # Game state
    current_room = "Lobby"
    inventory = []

    show_instructions()

    # Main loop: runs until the player wins, loses, or exits
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip()
        lowered = command.lower()

        # Blank input
        if not command:
            print("Please enter a command.")

        # Exit command
        elif lowered == "exit":
            print("Thanks for playing.")
            break

        # Movement command
        elif lowered == "go" or lowered.startswith("go "):
            direction = command[2:].strip().capitalize()

            if not direction:
                print("Specify a direction, for example 'go North'.")
            elif direction not in valid_directions:
                print("Invalid direction. Use North, South, East, or West.")
            elif direction not in rooms[current_room]:
                print(f"You can't go that way from the {current_room}.")
            else:
                current_room = rooms[current_room][direction]
                print(f"You move {direction} to the {current_room}.")

                # Win/loss check happens only when entering the villain's room
                if current_room == "Server Room":
                    if len(inventory) == total_items:
                        print("You have all the evidence. The Phantom is exposed.")
                        print("You win!")
                    else:
                        print("The Phantom locks you out and wipes the evidence.")
                        print("You lose.")
                    break

        # Get-item command
        elif lowered == "get" or lowered.startswith("get "):
            requested = command[3:].strip()
            room_item = rooms[current_room]["item"]

            if not requested:
                print("Specify an item, for example 'get Access Badge'.")
            elif room_item and requested.lower() == room_item.lower():
                if room_item in inventory:
                    print(f"You already have the {room_item}.")
                else:
                    inventory.append(room_item)
                    print(f"You picked up the {room_item}.")
                    print(f"Items collected: {len(inventory)} of {total_items}")
            else:
                print(f"There is no {requested} in the {current_room}.")

        # Anything else
        else:
            print("Invalid command. Use 'go [direction]' or 'get [item]'.")


if __name__ == "__main__":
    main()
