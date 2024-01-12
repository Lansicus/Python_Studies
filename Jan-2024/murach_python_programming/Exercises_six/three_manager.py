
contact_list = [
    ["James", "888-888-8888", "James@email.com"],
    ["Gabriel", "777-777-7777", "Gabriel@email.com"],
    ["Robert", "999-999-9999", "Robert@email.com"]
]


def contacts():
    for item in contact_list:
        print(item)


def view():
    choice = input("Who are you looking for? ")
    found = False

    for contact in contact_list:
        if choice.lower() in contact[0].lower():
            found = True
            print("\n".join(contact))
            break

    if not found:
        print("We don't have records of this contact.")


def add():
    chosen_name = input("Who's name would you like to add? ")
    chosen_number = input("What is their phone number? ")
    chosen_email = input("What is their email? ")
    contact_list.append([chosen_name, chosen_number, chosen_email])
    print(f"{chosen_name}'s contact has been added.")


def delete():
    choice = input("Delete a contact by name or 'exit': ")
    if choice.lower() == "exit":
        return

    found = False
    for contact in contact_list:
        if choice.lower() in contact[0].lower():
            found = True
            contact_list.remove(contact)
            print(f"{choice}'s contact has been deleted.")
            break

    if not found:
        print("Contact not found.")


def menu():
    print("Contact Manager")
    print()
    print("Command Menu")
    print("list")
    print("view")
    print("add")
    print("delete")
    print("exit")

    while True:
        command = input("What would you like to do? ").lower()
        if command == "list":
            contacts()
        elif command == "view":
            view()
        elif command == "add":
            add()
        elif command == "delete":
            delete()
        elif command == "exit":
            print("Application closed")
            break
        else:
            print("Enter a valid command or 'exit'")


def main():
    menu()


if __name__ == "__main__":
    main()

