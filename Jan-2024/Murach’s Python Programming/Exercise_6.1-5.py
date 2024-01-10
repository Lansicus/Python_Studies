def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    print("Prime Number Checker")
    pick = round(input("Please enter an integer between 1 and 5000: "),1)
    if is_prime(pick):
        print(f"{pick} is a prime number")
    else:
        print(f"{pick} is NOT a prime number")
        print(f"It has {} factors: {}")

