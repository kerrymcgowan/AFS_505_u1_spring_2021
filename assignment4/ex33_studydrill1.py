def print_numbers(min, max):

    while min < max:
        print(f"At the top min is {min}")
        numbers.append(min)
        #numbers.append({min})
        min = min + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom min is {min}")

numbers = []
print_numbers(0, 6)

print("The numbers: ")

for num in numbers:
    print(num)
