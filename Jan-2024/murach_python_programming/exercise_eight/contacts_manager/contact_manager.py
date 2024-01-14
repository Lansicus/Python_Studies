# ---------------------------------------------------------------------------------------- IMPORTING/ CREATING JSON FILE
import os
import json
import re  # Import the regular expression module

CONTACT_FILE = "./contacts.json"


def contact_checker():
    if not os.path.exists(CONTACT_FILE):
        print("Could not find contacts file.")
        print("Creating file now")

        with open(CONTACT_FILE, "w") as file:
            json.dump([], file)


# ----------------------------------------------------------------------------------------------------- OPEN & LOAD JSON
def load_contacts():
    with open(CONTACT_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file)


# --------------------------------------------------------------------------------------------------------- ADD FUNCTION
def is_valid_name(name):
    return bool(re.match("^[a-zA-Z ]+$", name))


def is_valid_phone_number(phone_number):
    return bool(re.match("^[0-9-]+$", phone_number)) and 10 <= len(phone_number) <= 15


def is_valid_email(email):
    return bool(re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))


def add():
    contact_list = load_contacts()

    while True:
        chosen_name = input("Who's name would you like to add? ")

        if is_valid_name(chosen_name):
            break
        else:
            print("Invalid name. Please use only letter characters.")

    while True:
        chosen_number = input("What is their phone number? ")

        if is_valid_phone_number(chosen_number):
            break
        else:
            print("Invalid phone number. Please use only numbers and '-' characters.")

    while True:
        chosen_email = input("What is their email? ")

        if is_valid_email(chosen_email):
            break
        else:
            print("Invalid email. Please ensure it contains only letters, numbers, '@', and '.'.")

    contact_list.append([chosen_name, chosen_number, chosen_email])
    save_contacts(contact_list)
    print(f"{chosen_name}'s contact has been added.")


# ------------------------------------------------------------------------------------------------------ DELETE FUNCTION
def delete():
    contact_list = load_contacts()
    choice = input("Delete a contact by name or 'exit': ")
    if choice.lower() == "exit":
        return

    found = False
    for contact in contact_list:
        if choice.lower() in contact[0].lower():
            found = True
            contact_list.remove(contact)
            save_contacts(contact_list)
            print(f"{choice}'s contact has been deleted.")
            break

    if not found:
        print("Contact not found.")


# --------------------------------------------------------------------------------------------- VIEW AND SEARCH CONTACTS
def contacts():
    contact_list = load_contacts()
    for contact in contact_list:
        print(", ".join(contact), end="\n\n")


def search():
    contact_list = load_contacts()
    choice = input("Who are you looking for? ")
    found = False

    for contact in contact_list:
        if choice.lower() in contact[0].lower():
            found = True
            print(", ".join(contact))
            break

    if not found:
        print("We don't have records of this contact.")


# ---------------------------------------------------------------------------------------------------------- MENU & MAIN
def menu():
    print("Contact Manager")
    print()
    print("Command Menu")
    print("list - Show all")
    print("search - Find specific")
    print("add - Create new contact")
    print("delete - Delete a contact")
    print("exit - Exit program")
    print("")

    while True:
        contact_checker()
        command = input("What would you like to do? ").lower()
        if command == "list":
            contacts()
        elif command == "view":
            search()
        elif command == "add":
            add()
        elif command == "delete":
            delete()
        elif command == "exit":
            print("Application closed")
            break
        else:
            print("Enter a valid command or 'exit'.")


def main():
    menu()


if __name__ == "__main__":
    main()
