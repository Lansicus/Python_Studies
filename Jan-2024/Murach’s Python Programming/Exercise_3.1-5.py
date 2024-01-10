# # 3-1
# # Create a program that converts number grades to letter grades.
# keep_grading = "y"
#
# while keep_grading == "y":
#     points = float(input("What is the number grade? "))
#     if points > 87:
#         grade = "A"
#     elif points > 79:
#         grade = "B"
#     elif points > 66:
#         grade = "C"
#     elif points > 59:
#         grade = "D"
#     else:
#         grade = "F"
#
#     print(f"The grade is: {grade}")
#     keep_grading = input("Continue grading? y/n ")
#
# print("Closing grading application...")
#
#
#
#
#
# # ----------------------------------------------------------------------------------------------------------------------
# # 3-2
# # Create a program that calculates three options for an appropriate tip to leave after a meal
# # at a restaurant.
# meal_cost = float(input("What was the cost of your meal? "))
#
# first_tip = meal_cost * 0.15
# first_total = meal_cost + first_tip
#
# second_tip = meal_cost * 0.20
# second_total = meal_cost + second_tip
#
# third_tip = meal_cost * 0.25
# third_total = meal_cost + third_tip
#
# # Format the results to always display two decimal places
# formatted_first_tip = "{:.2f}".format(first_tip)
# formatted_first_total = "{:.2f}".format(first_total)
#
# formatted_second_tip = "{:.2f}".format(second_tip)
# formatted_second_total = "{:.2f}".format(second_total)
#
# formatted_third_tip = "{:.2f}".format(third_tip)
# formatted_third_total = "{:.2f}".format(third_total)
#
# print("Tip Calculator\n\n"
#       f"Cost of meal: {meal_cost:.2f}\n\n"
#       "15%\n"
#       f"Tip amount: {formatted_first_tip}\n"
#       f"Total amount: {formatted_first_total}\n\n"
#       "20%\n"
#       f"Tip amount: {formatted_second_tip}\n"
#       f"Total amount: {formatted_second_total}\n\n"
#       "25%\n"
#       f"Tip amount: {formatted_third_tip}\n"
#       f"Total amount: {formatted_third_total}\n")
#
#
#
#
# # ----------------------------------------------------------------------------------------------------------------------
# # 3-3
# #Create a program that calculates the coins needed to make change for the specified
# # number of cents.
# print("Change Calculator\n\n")
# more_change = 'y'
#
# while more_change == 'y':
#     valid_input = False
#
#     while not valid_input:
#         try:
#             change = int(input("Enter number of cents (0-99): \n\n"))  # Convert input to integer
#             if 0 <= change <= 99:
#                 valid_input = True  # Set the flag to True if the input is valid
#             else:
#                 print("Please enter a number between 0 and 99.")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     quarters = change // 25
#     dimes = (change % 25) // 10
#     nickels = ((change % 25) % 10) // 5
#     pennies = ((change % 25) % 10) % 5
#
#     print(f"Quarters: {quarters}\n"
#           f"Dimes: {dimes}\n"
#           f"Nickels: {nickels}\n"
#           f"Pennies: {pennies}\n")
#
#     more_change = input("Continue? (y/n): \n").lower()
#
# print("Bye!")
#
#
#
# # ----------------------------------------------------------------------------------------------------------------------
# # 3-4
# # Create a program that calculates the total cost of an order including shipping.
# print("===============================================================\n"
#       "Shipping Calculator\n"
#       "===============================================================\n")
#
# more_orders = 'y'
#
# while more_orders == 'y':
#     valid_input = False  # Initialize the flag
#
#     while not valid_input:
#         try:
#             cost_of_items = float(input("In number digits, What was the cost of your items? "))
#             if cost_of_items >= 0:
#                 valid_input = True  # Set the flag to True if the input is valid
#             else:
#                 print("Please enter a non-negative number.")
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")
#
#     if cost_of_items < 30.00:
#         shipping_cost = 5.95
#     elif 30.00 <= cost_of_items <= 49.99:
#         shipping_cost = 7.95
#     elif 50.00 <= cost_of_items <= 74.99:
#         shipping_cost = 9.95
#     else:
#         shipping_cost = 0.00
#
#     print("Cost of items ordered: {cost_of_items}\n"
#           f"Shipping Cost: {shipping_cost}\n"
#           f"Total Cost: {cost_of_items + shipping_cost}\n\n")
#     more_orders = input("Continue? (y/n) ")
#
# print("===============================================================\n"
#       "Bye!")
#

# ----------------------------------------------------------------------------------------------------------------------
# 3-5
# start_number = None
# while start_number is None or not (0 <= start_number < 100 and start_number.is_integer()):
#     start_number = float(input("Pick a number (0-99) for the small end of your range: "))
#
# stop_number = None
# while stop_number is None or not (0 <= stop_number < 100 and stop_number.is_integer() and stop_number > start_number):
#     stop_number = float(input("Now pick a number (0-99) for the high end of your range: "))
#
# start_number, stop_number = int(start_number), int(stop_number)
#
# print(f"Table of Powers\n\n"
#       f"Start number: {start_number}\n"
#       f"Stop number: {stop_number}\n\n"
#       f"Number\tSquared\tCubed\n"
#       f"======\t======\t======")
#
# for i in range(start_number, stop_number + 1):
#     squared = i ** 2
#     cubed = i ** 3
#     print(f"{i}\t{squared}\t{cubed}")


#----------------------------------------------------------------------------------------------------------------------
# Just YEE-HAW'n
while True:
    try:
        start_num = int(input("Enter the start integer: "))
        stop_num = int(input("Enter the stop integer: "))

        if start_num <= stop_num and stop_num - start_num < 10:
            break
        else:
            print("Error: Start integer should be less than stop integer, and the difference should be less than 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter integers.")

print("Number\tSquare\tCube")
print("======  ======  ====")

for num in range(start_num, stop_num + 1):
    square = num ** 2
    cube = num ** 3
    print(f"{num}\t\t{square}\t\t{cube}")

