import random

ALL_ITEMS_FILE = "all_items.txt"
INVENTORY_FILE = "wizard_inventory.txt"

# Menu function
def menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

# TODO: Read the input file and convert to list
def read_all_items():
    with open(ALL_ITEMS_FILE) as file:
        all_items = file.readlines()
    return all_items

def read_inventory():
    with open(INVENTORY_FILE) as file:
        inventory = file.readlines()
    return inventory


# TODO: Write function to convert list to file
def write_file(inventory):
    with open(INVENTORY_FILE, "w") as file:
        for item in inventory:
            file.write(f"{item}")
        print(f"Write to {INVENTORY_FILE} successful.")


# TODO: Drop function
def drop(inventory):
    show(inventory)
    index = int(input("Number: "))
    if index < 1 or index > len(inventory):
        print("Invalid movie number.\n")
    else:
        item = inventory.pop(index - 1)
        write_file(inventory)
        print(f"{item} was deleted.\n")


# TODO: Walk function
def walk(inventory, all_items):
    remaining_items = []
    for item in all_items:
        if item not in inventory:
            remaining_items.append(item)
    random_item = random.choice(remaining_items)

    print(f"While walking down a path, you see {random_item}")
    choice = input("Do you want to grab it? (y/n): ")
    if choice.lower() == 'y':
        if len(inventory) == 4:
            print("Can't add new items. Inventory full. Delete existing item")
        else:
            inventory.append(random_item)
            write_file(inventory)
            print(f"{random_item} added to Inventory")


# TODO: Show function
def show(inventory):
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}", end="")
    print()


def main():
    print("The Wizard Inventory program")
    menu()

    inventory = read_inventory()
    all_items = read_all_items()

    while True:
        cmd = input("Command: ")
        if cmd.lower() == "show":
            show(inventory)
        elif cmd.lower() == "walk":
            walk(inventory, all_items)
        elif cmd.lower() == "drop":
            drop(inventory)
        elif cmd.lower() == "exit":
            break


main()