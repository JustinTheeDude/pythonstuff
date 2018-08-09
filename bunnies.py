from itertools import combinations
plates = [5,5,3]


def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for i in combinations(plates, len(plates)):
        sumOfPlates = sum(plates)
        if sumOfPlates % 3 == 0:
            print 'good'
        if sumOfPlates % 3 == 1:
            platelist = [n for n in plates]
            platelist.pop(platelist.index(-max([-u for u in platelist if u % 3 == 2])))
            sortedp = sorted(platelist, key=int, reverse=True)

        if sumOfPlates % 3 == 2:
            platelist = [n for n in plates]
            platelist.pop(platelist.index(-max([-u for u in platelist if u % 3 == 2])))
            sortedp = sorted(platelist, key=int, reverse=True)

        print int(''.join(map(str, sortedp)))

bunnies(plates)
