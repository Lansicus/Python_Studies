# import six_two as demo


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
        pick = input("Enter an integer between 1 and 5000, or type 'exit': ")

        if pick.lower() == 'exit':
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
                print("Invalid input. Enter an integer or 'exit'.")

            if not keep_going():
                break


def prime_number_checker():
    prime_number_title()
    prime_number_prompt()


# ----------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTION
def main():
    prime_number_checker()


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
