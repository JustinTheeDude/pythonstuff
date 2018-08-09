from itertools import combinations
plates = [8, 2, 1, 4, 1, 2, 5]


def bunnies(plates):
    for i in combinations(plates, len(plates)):
        sumOfPlates = sum(plates)
        if sumOfPlates % 3 == 1:
            platelist = [n for n in i]
            try:
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 1])))
            except ValueError:
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 2])))
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 2])))
            sortedp = sorted(platelist, key=int, reverse=True)

        if sumOfPlates % 3 == 2:
            platelist = [n for n in plates]
            try:
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 2])))
            except ValueError:
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 1])))
                platelist.pop(platelist.index(min(
                    [u for u in platelist if u % 3 == 1])))
            sortedp = sorted(platelist, key=int, reverse=True)

        return ''.join(map(str, sortedp))


for count in xrange(10):
    something = [int(x) for x in list("{}".format(count))]
    ans = bunnies(plates)
    print("{} : {}".format(count, ans))
