def main():
    print("Tip Calculator")
    print()
    print("INPUT")
    while True:
        try:
            meal_cost = round(float(input("Cost of meal: ")), 2)
            if meal_cost <= 0:
                print("Meal cost must be greater than zero.")
                continue  # Restart the loop if input is invalid
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Restart the loop if input is invalid

        try:
            tip_percent = int(input("Tip percent: "))
            if tip_percent <= 0:
                print("Tip must be a whole number greater than zero.")
                continue  # Restart the loop if input is invalid
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
            continue  # Restart the loop if input is invalid

        tip_amount = (tip_percent / 100) * meal_cost
        total = tip_amount + meal_cost

        print(f"Cost of meal: {meal_cost}")
        print(f"Tip percent: {tip_percent}%")
        print(f"Tip amount: {tip_amount}")
        print(f"Total amount: {total}")
        break  # Exit the loop if all inputs are valid

main()
