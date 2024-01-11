def prompts():
    print("The Quarterly Sales Program")
    print()
    q1 = round(float(input("Enter sales for Q1: ")), 2)
    q2 = round(float(input("Enter sales for Q2: ")), 2)
    q3 = round(float(input("Enter sales for Q3: ")), 2)
    q4 = round(float(input("Enter sales for Q4: ")), 2)

    total = q1 + q2 + q3 + q4
    average = total / 4

    # Find the lowest and highest sales
    quarters = [q1, q2, q3, q4]
    lowest = min(quarters)
    highest = max(quarters)

    print()
    print(f"Total: \t\t\t{total}")
    print(f"Average Quarter: \t{average}")
    print(f"Lowest Quarter: \t{lowest}")
    print(f"Highest Quarter: \t{highest}")


def main():
    prompts()


if __name__ == '__main__':
    main()
