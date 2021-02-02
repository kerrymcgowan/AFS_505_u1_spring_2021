def make_dinner(soup, salad):
    print(f"I will have a {soup} soup.")
    print(f"I will have a {salad} salad.")

# 1
make_dinner("chowder", "kale")

# 2
make_dinner(soup = "chowder", salad = "kale")

# 3
type_of_soup = "chowder"
type_of_salad = "kale"

make_dinner(type_of_soup, type_of_salad)

# 4
make_dinner(type_of_soup, "kale")

# 5
make_dinner("chowder", type_of_salad)

# 6
from sys import argv
scripts, yummy_soup, yummy_salad = argv
make_dinner(yummy_soup, yummy_salad)

# 7
m sys import argv
scripts, yummy_soup = argv
make_dinner(yummy_soup, "kale")

# 8
from sys import argv
scripts, yummy_salad = argv
make_dinner("chowder", yummy_salad)
