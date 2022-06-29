import itertools

one = ("а", "в", "г")
two = ("е", "и", "к")
three = ("л", "н", "о")
four = ("п", "р", "с")
five = ("т", "у", "щ")
six = ("ь", "я", "*")


# lines
l1 = itertools.product(one, one, five, three, two, four, one, five, two, six)
l2 = itertools.product(one, six, five, six, three, three, five, three, six, one)
l3 = itertools.product(five, four, two, four, two, five, one, three, two, two)
l4 = itertools.product(three, six, five, five, five, one, six, five, six, three)
l5 = itertools.product(four, two, one, three, six, three, three, four, five, six)


# columns
c1 = itertools.product(one, one, five, three, four)
c2 = itertools.product(one, six, four, six, two)
c3 = itertools.product(five, five, two, five, one)
c4 = itertools.product(three, six, four, five, three)
c5 = itertools.product(two, three, two, five, six)
c6 = itertools.product(four, three, five, one, three)
c7 = itertools.product(one, five, one, six, three)
c8 = itertools.product(five, three, three, five, four)
c9 = itertools.product(two, six, two, six, five)
c10 = itertools.product(six, one, two, three, six)


# keyword
orange = ['к', 'с', 'у']
blue = ['п', 'л', 'ь']
purple = ['р', 'о', 'т']

kw = itertools.product(orange, orange, orange, blue, blue, blue, purple, purple, purple)
