# create a program that reads a list of rules from a file and displays them

# Open the file in read mode
with open('rules.txt', 'r') as file:
    # Read the entire content of the file
    data = file.read()

# Now, 'data' contains the content of the file
print(data)
