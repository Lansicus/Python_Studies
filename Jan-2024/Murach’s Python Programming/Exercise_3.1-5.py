while True:
    start_number = input("What is your start number? ")
    if start_number.isdigit() and len(start_number) < 100:
        break
    else:
        print("Please use only number digits less than 100")

while True:
    stop_number = input("What is your start number? ")
    if stop_number.isdigit() and len(stop_number) < 100:
        break
    else:
        print("Please use only number digits less than 100")

input("What is your end number?")

print(f"Table of Powers/n/n"
      f"Start number: {start_number}/n"
      f"Stop number: {stop_number}/n/n"
      f"Number/tSquared/tCubed/n"
      f"======/t======/t======/n"
      )
