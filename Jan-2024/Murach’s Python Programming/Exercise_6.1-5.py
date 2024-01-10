# ----------------------------------------------------------------------------------------------------------------------
# TRY AGAIN FUNCTION?
def keep_going():
    while True:
        response = input("Try again? (y/n) ")
        if response.lower() == "n":
            print("Bye!")
            return False
        elif response.lower() == "y":
            return True
        else:
            print("Enter a valid input")


# ----------------------------------------------------------------------------------------------------------------------
# PRIME NUMBER
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_number_title():
    print("Prime Number Checker")


def prime_number_prompt():
    while True:
        pick = input("Enter an integer between 1 and 5000, or 'no' to exit: ")

        if pick.lower() == 'no':
            print("Application closed")
            break
        else:
            try:
                pick = int(pick)
                if 1 <= pick <= 5000:
                    result = is_prime(pick)
                    if result:
                        print(f"{pick} is a prime number")
                    else:
                        print(f"{pick} is NOT a prime number")
                        factors = [i for i in range(1, pick + 1) if pick % i == 0]
                        num_of_factors = len(factors)
                        print(f"It has {num_of_factors} factors: {factors}")
                else:
                    print("Enter an integer between 1 and 5000.")
            except ValueError:
                print("Invalid input. Enter an integer or 'no'.")

            if not keep_going():
                break


def prime_number_checker():
    prime_number_title()
    prime_number_prompt()




# ----------------------------------------------------------------------------------------------------------------------
# WIZARD SHLIZARD
inventory = ["Wizard Hat", "fire staff", "running shoes", "sprint potion"]
ground_items = ["dire claw", "nice pelt", "big hammer"]
def take_command():
    selection = input("What is your command? ")
    return selection
def command(choice):
    if choice.lower() == "show":
        for item in inventory:
            print(item)
    if choice.lower() == "grab":
        if len(inventory) = 5:
            print("you are carrying too much already")
            break
        else:
            for index, item in enumerate(ground_items, start=1):
                print(f"{index}. {item}")
                grab_choice = input("What would you like to pick up..? ")
                inventory.append(grab_choice)

        inventory.append()
    if choice.lower() == "edit":
        inventory[] =
    if choice.lower() == "drop":
        inventory.remove()
    if choice.lower() == "exit":
        break
    else:
        print("Enter a valid command or exit")

def wizard_title():
    print("The Wizard Inventory Program")
    print()
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - drop an item")
    print("exit - Exit program")

    print(f"Command: {command(take_command())}")

    # selecti0on = take_command()
    #
    # if selecti0on == :



# ----------------------------------------------------------------------------------------------------------------------
#MAIN FUNCTION
def main():
    # prime_number_checker()


main()

# ----------------------------------------------------------------------------------------------------------------------
# HONORABLE MENTIONS
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# def prime_number_title():
#     print("Prime Number Checker")
#
# def prime_number_prompt():
#     while True:
#         pick = round(input("Say 'no' or, Enter an integer between 1 and 5000: "),1)
#         if pick.lower() == 'no':
#             print("application closed")
#             break
#         elif 1 <= pick <= 5000 and pick.isdigit():
#             is_prime(pick)
#             if is_prime():
#                 print(f"{pick} is a prime number")
#             else:
#                 print(f"{pick} is NOT a prime number")
#                 print(f"It has {num_of_factors} factors: {list_of_factors}")
#         else:
#             print("Say 'no' or, Enter an integer between 1 and 5000: ")
