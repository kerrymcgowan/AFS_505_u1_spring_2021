mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine  = "Living reflection of a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
