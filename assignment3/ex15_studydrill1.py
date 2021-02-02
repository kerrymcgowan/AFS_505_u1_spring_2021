# Import the argv object from the sys library
from sys import argv

# Write out the argument variables
script, filename = argv

# Make the file object filename and assign it to the variable txt
txt = open(filename)

# Print an f-string
print(f"Here's your file {filename}:")
# Call read function on the variable txt and print result
print(txt.read())

# Print a string
print("Type the filename again:")
# Ask for input when the variable file_again is called
file_again = input("> ")

# Make the file object file_again and assign it to the variable txt_again
txt_again = open(file_again)

# Call the read function on the variable txt_again and print result
print(txt_again.read())
