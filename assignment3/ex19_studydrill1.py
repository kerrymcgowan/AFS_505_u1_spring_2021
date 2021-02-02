# Make a funciton
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# Print a string
print("We can just give the function numbers directly:")
# Call the function cheese_and_crackers
cheese_and_crackers(20, 30)


# Print a string
print("OR, we an use variables from our script:")
# Make variables
amount_of_cheese = 10
amount_of_crackers = 50

# Call the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Print a string
print("We can een do math inside too:")
# Call the function cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)


# Print a string
print("And we can combine the two, variables and math:")
# Call the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
