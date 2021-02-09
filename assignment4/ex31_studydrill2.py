print("""Let's figure out what dessert you should make.
Should you pick a old or new recipe?""")

recipe=input("> ")

if recipe == "old":
    print("1. Put on a podcast while baking.")
    print("2. Watch The Great British Baking Show while baking.")

    entertainment=input("> ")

    if entertainment == "1":
        print("Listen to the new episode of This American Life.")
    elif entertainment == "2":
        print("Aren't Paul and Merry Berry funny?")
    else:
        print("Put some good music on.")

elif recipe == "new":
    print("1. Make tiramisu.")
    print("2. Make key lime pie.")
    print("3. Make a chocolate peanut butter bundt cake.")

    recipe=input("> ")

    if recipe == "1":
        print("Did you remember to buy ladyfinger cookies?")
    elif recipe == "2":
        print("We don't get key limes in WA, so it's really a lime pie.")
    elif recipe == "3":
        print("This should be delicious.")
    else:
        print("Try something else.")

else:
    print("I'm feeling too lazy to bake anything.")
