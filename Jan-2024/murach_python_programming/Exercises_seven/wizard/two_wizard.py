with open('all_items.txt', 'r') as file:
    # Read the entire content of the file
    ground = file.read()

# Modify the content as needed
# For example, remove a specific substring
modified_content = ground.replace("substring_to_remove", "")

# Open the file in write mode and write the modified content back
with open('all_items.txt', 'w') as file:
    file.write(modified_content)

with open('wizard_inventory.txt', 'r') as file:
    pocket = file.readlines()


# -----------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
def inventory():
    print("Wizard's Inventory:")
    with open('wizard_inventory.txt', 'r') as file:
        pocket = file.readlines()
    for line in pocket:
    # Do something with each line, for example print it
        print(line.strip())  # strip() removes leading and trailing whitespaces

def telescope():
    with open('all_items.txt', 'r') as file:
        ground = file.readlines()
    for line in ground:
    # Do something with each line, for example print it
        print(line.strip())  # strip() removes leading and trailing whitespaces





# ---------------------------------------------------------------------------------------------------------------------
def drop():
    # Read 'pocket' from 'wizard_inventory.txt'
    with open('wizard_inventory.txt', 'r') as pocket_file:
        pocket = pocket_file.read()

    inventory()
    choice = input("Drop item by exact name or 'exit': ")

    if choice.lower() == 'exit':
        return
    elif choice in pocket:
        # Step 1: Remove the item from 'pocket'
        modified_content = pocket.replace(f"{choice}\n", "")
        with open('wizard_inventory.txt', 'w') as pocket_file:
            pocket_file.write(modified_content)

        # Step 2: Append the item to 'ground'
        with open('all_items.txt', 'a') as ground_file:
            ground_file.write(f"{choice}\n")

        print(f"{choice} dropped from pocket to ground.")
    else:
        print("Enter a correct item name or 'exit'")


# ---------------------------------------------------------------------------------------------------------------------
def walk():
    # Assuming 'ground' and 'pocket' are read from corresponding files as before
    with open('all_items.txt', 'r') as ground_file:
        ground = ground_file.read()

    print(f"While walking, you discover {ground}")

    if len(pocket) == 4:
        choice = input("Inventory is full. Would you like to drop something? (y/n) ").lower()
        if choice == 'n':
            return
        elif choice == 'y':
            drop()

    choice = input("Pick it up? (y/n) ").lower()

    if choice == 'n':
        return
    elif choice == 'y' and choice in ground:
        # Remove the chosen item from 'ground'
        modified_content = ground.replace(f"{choice}\n", "")
        with open('all_items.txt', 'w') as ground_file:
            ground_file.write(modified_content)

        # Append the chosen item to 'pocket'
        with open('wizard_inventory.txt', 'a') as pocket_file:
            pocket_file.write(f"{choice}\n")

        print(f"{choice} picked up and added to pocket.")
    else:
        print("Use correct inputs or 'exit'")


# ----------------------------------------------------------------------------------------------------------------------
def wizard_title():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("show - Show held items")
    print("telescope - Show ground items")
    print("walk - Walk down the path")
    print("drop - Drop an item")
    print("exit - Exit program")

    while True:
        command = input("What is your command? ").lower()

        if command == "show":
            inventory()
        elif command == "telescope":
            telescope()
        elif command == "walk":
            walk()
        elif command == "drop":
            drop()
        elif command == "exit":
            print("Application closed.")
            break
        else:
            print("Enter a valid command or 'exit'.")


# Call the function to start the program
def main_Wiz():
    wizard_title()


main_Wiz()
