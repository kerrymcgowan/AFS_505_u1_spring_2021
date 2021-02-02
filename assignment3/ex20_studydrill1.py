# Import the argv object from the sys library
from sys import argv

# Write out the argument variables
script, input_file = argv

# Make a function to read a file
def print_all(f):
    print(f.read())

# Make a function to set pointer to the beginning
def rewind(f):
    f.seek(0)

# print line count and the line content
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Make the file object input_file and assign it to the variable current_file
current_file = open(input_file)

# Print a string
print("First let's print the whole file:\n")

# Call the function print_all
print_all(current_file)

# Print a string
print("Now let's rewind, kind of like a tape.")

# Call the function rewind
rewind(current_file)

# Print a string
print("Let's print three lines:")

# Set a variable
current_line = 1
# Call the function print_a_line
print_a_line(current_line, current_file)

# Set a variable
current_line = current_line + 1
# Call the function print_a_line
print_a_line(current_line, current_file)

# Set a variable
current_line = current_line + 1
# Call the function print_a_line
print_a_line(current_line, current_file)
