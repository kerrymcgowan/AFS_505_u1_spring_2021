# make a variable
formatter = "{} {} {} {}"

# Call the format function, which replaces the curly brackets in formatter with 4 new arguments
print(formatter.format(1, 3, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
