from random import randint


# 4.1
# Even or odd Checker

def check_even_odd():
    # Get user input
    user_input = int(input("Enter a number: "))

    # Check if the input is even or odd
    if user_input % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    # Display the result
    print(f"The number {user_input} is {result}.")


# ---------------------------------------------------------------------------------------------------------------------
# 4.2
def hike_title():
    print("Hike calculator\n\n")


def miles_to_feet(miles):
    feet = miles * 5280
    return feet


def hike_calculator():
    hike_title()
    miles = float(input("How many miles did you walk? \n"))
    feet = miles_to_feet(miles)
    print(f"You have walked {feet} feet\n")


# Call the function to execute the hike calculator


# ---------------------------------------------------------------------------------------------------------------------
# 4.3
def meter_feet_title():
    print("Feet and Meters Converter")


def meter_to_feet(meter):
    feet = meter / 0.3048
    return feet


def feet_to_meter(feet):
    meters = feet * 0.3048
    return meters


def conversions_method():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

    while True:
        choice = input("Select a conversion (a/b/no): ")

        if choice.lower() == "a":
            feet = float(input("Enter feet: "))
            print(f"{feet} feet is approximately {round(feet_to_meter(feet), 2)} meters")
        elif choice.lower() == "b":
            meter = float(input("Enter meters: "))
            print(f"{meter} meters is approximately {round(meter_to_feet(meter), 2)} feet")
        elif choice.lower() == "no":
            print("Closing Converter")
            break
        else:
            print("Enter 'a', 'b', or 'no'.")


def feet_and_meters_converter():
    meter_feet_title()
    conversions_method()


# ---------------------------------------------------------------------------------------------------------------------
# 4.4
# Sales Tax Calculator


# ---------------------------------------------------------------------------------------------------------------------
# 4.5
# DUNGEON DICE ROLLER
def dice_roller():
    keep_rolling = "y"
    print("Dice Roller\n\n")
    roll_dice = input("Roll the dice? (y/n) \n\n")
    while keep_rolling.lower() == "y":

        try:
            if roll_dice.lower() == "n":
                break
            elif roll_dice.lower() == "y":
                rand_one = randint(1, 6)
                rand_two = randint(1, 6)
                snake = False
                box = False

                if rand_one == 1 and rand_two == 1:
                    snake = True
                if rand_one == 6 and rand_two == 6:
                    box = True

                print(f"Die 1: {rand_one}")
                print(f"Die 2: {rand_two}")
                print(f"Total: {rand_one + rand_two}")

                if snake:
                    print("Snake eyes!")
                elif box:
                    print("Boxcar!")

                keep_rolling = input("Roll again? (y/n)\n\n ")

        except ValueError:
            print("Enter 'y' or 'n'")


# ---------------------------------------------------------------------------------------------------------------------
# 4.6
# Create a program that checks whether a number is a prime number and displays the total
# number of factors if it is not a prime number.


# print("Prime Number Checker")
# given_number = input("Please enter an integer between 1 and 5000: ")
#
#
# def is_prime_with_divisors(number):
#     if number <= 1:
#         return False, 0
#     elif number == 2:
#         return True, 2
#     elif number % 2 == 0:
#         return False, 2
#     else:
#         # Check for factors up to the square root of the number
#         count_divisors = 0
#         for i in range(1, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 count_divisors += 1
#                 if i != number // i:  # Handle the case where i is not equal to the other divisor
#                     count_divisors += 1
#
#         return count_divisors == 2, count_divisors


# ----------------------------------------------------------------------------------------------------------------------
def main():
    check_even_odd()
    hike_calculator()
    dice_roller()
    feet_and_meters_converter()


main()
