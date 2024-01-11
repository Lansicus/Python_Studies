inventory = ["Wizard Hat", "fire staff", "running shoes", "sprint potion"]
ground_items = ["dire claw", "nice pelt", "big hammer"]


def show_inventory():
    for item in inventory:
        print(item)

def show_ground():
    for item in inventory:
        print(item)


def grab_item():
    if len(inventory) == 5:
        print("You are carrying too much already")
        return

    for index, item in enumerate(ground_items, start=1):
        print(f"{index}. {item}")

    grab_choice = input("Enter an item's number to take or 'exit': ")
    if grab_choice.lower() == 'exit':
        return

    try:
        selected_index = int(grab_choice) - 1
        if 0 <= selected_index < len(ground_items):
            choice = ground_items.pop(selected_index)
            inventory.append(choice)
        else:
            print("Invalid item number")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")


def edit_inventory():
    for index, item in enumerate(inventory, start=1):
        print(f"{index}. {item}")

    edit_choice = input("Enter an item number to edit or 'exit': ")
    if edit_choice.lower() == 'exit':
        return

    try:
        selected_index = int(edit_choice) - 1
        if 0 <= selected_index < len(inventory):
            new_value = input("What will it be changed to? ")
            inventory[selected_index] = new_value
        else:
            print("Invalid item number")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")


def drop_item():
    if len(inventory) == 1:
        print("You must not clear your inventory.")
        return

    for index, item in enumerate(inventory, start=1):
        print(f"{index}. {item}")

    drop_choice = input("Enter an item number to drop or 'exit': ")
    if drop_choice.lower() == 'exit':
        return

    try:
        selected_index = int(drop_choice) - 1
        if 0 <= selected_index < len(inventory):
            dropped_item = inventory.pop(selected_index)
            ground_items.append(dropped_item)
        else:
            print("Invalid item number")
    except ValueError:
        print("Invalid input. You may enter a valid item number or 'exit'.")


def wizard_title():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("show - Show all items")
    print("look - Show nearby items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

    while True:
        command = input("What is your command? ").lower()

        if command == "show":
            show_inventory()
        elif command == "look":
            show_ground()
        elif command == "grab":
            grab_item()
        elif command == "edit":
            edit_inventory()
        elif command == "drop":
            drop_item()
        elif command == "exit":
            print("Application closed.")
            break
        else:
            print("Enter a valid command or 'exit'.")


# Call the function to start the program
def main_Wiz():
    wizard_title()


main_Wiz()
