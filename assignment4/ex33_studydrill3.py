def print_numbers(min, max, increment):

    while min < max:
        print(f"At the top min is {min}")
        numbers.append(min)
        #numbers.append({min})
        min = min + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom min is {min}")

numbers = []
print_numbers(0, 10, 3)

print("The numbers: ")

for num in numbers:
    print(num)
