plates = [8, 5, 1, 8, 3, 4]


def bunnies(plates):
    sortedp = sorted(plates, key=int, reverse=True)
    sumOfPlates = sum(plates)
    if sumOfPlates % 3 == 1:
        try:
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 1])))
        except ValueError:
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 2])))
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 2])))

    if sumOfPlates % 3 == 2:
        try:
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 2])))
        except ValueError:
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 1])))
            sortedp.pop(sortedp.index(min(
                [u for u in sortedp if u % 3 == 1])))

    return ''.join(map(str, sortedp))


for count in xrange(100000):
    plates = [int(x) for x in list("{}".format(count))]
    ans = bunnies(plates)
    print("{} : {}".format(count, ans))
