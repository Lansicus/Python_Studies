
# 2-1: Password Generator

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Ensure input for birth year is four long and numeric
while True:
    birth_year = input("What is your birth year? ")
    if birth_year.isdigit() and len(birth_year) == 4:
        break
    else:
        print("Please enter a valid 4-digit numeric birth year.")

# take last two digits of birth year
last_two_digits = birth_year[-2:]
# temp password
temporary_password = f"{first_name}*{last_name}{last_two_digits}"

# Display registration form and welcome message
print(f"\nRegistration Form\n\n"
      f"First Name:\t{first_name}\n"
      f"Last Name:\t{last_name}\n"
      f"Birth year:\t{birth_year}\n\n"
      f"Welcome {first_name} {last_name}!\n"
      f"Your registration is complete.\n"
      f"Your temporary password is: {temporary_password}\n\n\n")




# 2-2: Pay Check Calculator

hours_worked = float(input("How many hours have you worked this week? (Use only number digits) "))
hourly_pay_rate = float(input("What is your hourly pay rate? "))
gross_pay = hours_worked * hourly_pay_rate

tax_rate = 0.18
tax_amount = gross_pay * tax_rate
take_home = gross_pay - tax_amount

print(f"\nPay Check Calculator\n"
      f"Hours Worked:\t{hours_worked}\n"
      f"Hourly Pay Rate: {hourly_pay_rate}\n\n"
      f"Gross Pay:\t{gross_pay}\n"
      f"Tax Rate:\t{tax_rate}\n"
      f"Tax Amount:\t{tax_amount}\n"
      f"Take Home Pay:\t{take_home}\n\n")



# 2-3: Tip Calculator

cost_of_meal = float(input("What was the cost of your meal? "))
tip_percent = float(input("What percent would you like to tip? "))

tip_amount = cost_of_meal * (tip_percent / 100)
total_amount = cost_of_meal + tip_amount

print(f"\nTip Calculator\n\n"
      f"Cost of meal:\t{cost_of_meal} \n"
      f"Tip percent: {tip_percent} \n\n"
      f"Tip amount:\t{tip_amount} \n"
      f"Total amount:\t{total_amount} \n\n")





# 2-4
price64oz = 5.99
size64oz = 64

price32oz = 3.50
size32oz = 32

print(f"\nPrice Comparison\n\n \
    Price of 64 oz size: {price64oz} \n \
    Price of 32 oz size: {price32oz} \n\n \
    \
    Price per oz (64 oz): {float(price64oz / size64oz)} \n \
    Price per oz (32 oz): {float(price64oz / size64oz)} \n ")


# 2-5
milesTraveled = (input("How many miles did you travel? "))
milesPerHour = (input("What mph were you traveling at? "))

print(f"\nTravel Time Calculator\n\n \
      Enter miles: {milesTraveled} \n \
      Enter miles per hour: {milesPerHour} \n\n \
      \
      Estimated travel time\n \
      Hours: {float(milesTraveled) / float(milesPerHour)} \n \
      Minutes: {float(milesTraveled) % float(milesPerHour) * 60 // float(milesPerHour)} ")
