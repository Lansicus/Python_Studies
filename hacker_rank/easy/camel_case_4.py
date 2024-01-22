# -------------------------------------------------------------------------------------------------------- BEST SOLUTION
import sys
import re


# Function to process each input line
def process_input_line(line):
    # Split the input line into operation, type, and name
    operation, typ, name = line.strip("()").split(";")

    # Check if the name contains spaces and handle accordingly
    if " " in name:
        name = name.split()
    else:
        # Use regular expression to find all words in camel case
        name = re.findall("[A-Z]?[a-z]+", name)

    # Perform the specified operation
    if operation == "S":
        # If 'split', join words in lowercase with space
        return " ".join([w.lower() for w in name])
    else:
        # If 'combine', create camel case string based on type
        camel_case = name[0].lower() + "".join([w.capitalize() for w in name[1:]])
        if typ == "M":
            return camel_case + "()"
        if typ == "C":
            return "".join([w.capitalize() for w in name])
        return camel_case


# Main function to read from STDIN and print to STDOUT
def main():
    # Read the complete input from STDIN and remove carriage returns
    complete_input = sys.stdin.read().replace("\r", "")

    # Process each input line using the process_input_line function
    results = map(process_input_line, complete_input.split("\n"))

    # Print the results to STDOUT
    print("\n".join(results))


# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------- RULES
# First Letter:
# 'S' = Separate the words
# 'C' = Combine the words
#
# Second Letter:
# 'M' = Method
# 'V' = Variable
# 'C' = Class
#
# Letter Combos:
# 'S;M;' = separate words before capital letters & Lowercase all words & remove '()'
# 'S;C;' = separate words before capital letters & Lowercase all words
# 'S;V;' = separate words before capital letters & Lowercase all words
#
# 'C;M;' = capitalize every word after the first & then remove blank space & end with ()
# 'C;C;' = capitalize the start of every word & then remove blank space between
# 'C;V;' = capitalize every word after the first & then remove blank space


# ------------------------------------------------------------------------------------------------ EXAMPLE INPUT/ OUTPUT
# EXAMPLE 1
# INPUT: 'S;M;plasticCup()'
# OUTPUT: 'plastic cup'

# EXAMPLE 2
# INPUT: 'C;V;mobile phone'
# OUTPUT: 'mobilePhone'

# EXAMPLE 3
# INPUT: 'C;C;coffee machine'
# OUTPUT: 'CoffeeMachine'

# EXAMPLE 4
# INPUT: 'S;C;LargeSoftwareBook'
# OUTPUT: 'large software book

# EXAMPLE 5
# INPUT: 'C;M;white sheet of paper'
# OUTPUT: 'whiteSheetOfPaper();

# EXAMPLE 6
# INPUT: 'S;V;pictureFrame'
# OUTPUT: 'picture frame'


# ------------------------------------------------------------------------------------------------- HONORABLE MENTIONS 1
# import sys
# import re
#
# # Iterate over each line of input read from standard input
# for l in sys.stdin.read().replace("\r", "").split("\n"):
#     # Split each line into three parts using semicolons
#     m, t, s = l.split(";")
#
#     # Use regular expression to find all words in the camel case string
#     s = [*re.findall("[A-Z]?[a-z]+", s)]
#
#     # Check the operation type
#     if m == 'S':  # Split operation
#         # Print the space-delimited list of words in lowercase
#         print(*[x.lower() for x in s], sep=" ")
#     else:
#         if t == "V":  # Combine variable name
#             # Combine the words into camel case, capitalizing the first letter of each word except the first
#             print(s[0] + "".join([x.capitalize() for x in s[1:]]))
#         elif t == "M":  # Combine method name
#             # Combine the words into camel case, capitalizing the first letter of each word except the first,
#             # and append empty set of parentheses
#             print((s[0] + "".join([x.capitalize() for x in s[1:]]) + "()"))
#         else:  # Combine class name
#             # Combine the words into camel case, capitalizing the first letter of each word
#             print("".join([x.capitalize() for x in s]))


# ------------------------------------------------------------------------------------------------- HONORABLE MENTIONS 2
# import sys
# import re
#
# # Function to process each input line
# def process_input_line(line):
#     # Split the input line into operation, type, and name
#     operation, typ, name = line.strip("()").split(";")
#
#     # Check if the name contains spaces and handle accordingly
#     if " " in name:
#         name = name.split()
#     else:
#         # Use regular expression to split camel case
#         name = re.split("(?<=[a-z])(?=[A-Z])", name)
#
#     # Perform the specified operation
#     if operation == "S":
#         # If split, join words in lowercase with space
#         return " ".join([w.lower() for w in name])
#     else:
#         # If combine, create camel case string based on type
#         camel_case = name[0].lower() + "".join([w.capitalize() for w in name[1:]])
#         if typ == "M":
#             return camel_case + "()"
#         if typ == "C":
#             return "".join([w.capitalize() for w in name])
#         return camel_case
#
# # Main function to read from STDIN and print to STDOUT
# def main():
#     # Read the complete input from STDIN and remove carriage returns
#     complete_input = sys.stdin.read().replace("\r", "")
#
#     # Process each input line using the process_input_line function
#     results = list(map(lambda i: process_input_line(i), complete_input.split("\n")))
#
#     # Print the results to STDOUT
#     print("\n".join(results))
#
# # Ensure that the main function is called when the script is executed
# if __name__ == "__main__":
#     main()
#
