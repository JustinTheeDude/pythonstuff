from itertools import combinations
plates = [8, 5, 1, 8, 3, 4]


def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for i in combinations(plates, len(plates)):
        sortedPlates = sorted(plates, key=int, reverse=True)
        platestring = ''.join(map(str, sortedPlates))
        sumOfPlates = sum(plates)
        if sumOfPlates % 3 == 0:
            print 'good'
        if sumOfPlates % 3 == 2:
            newList = []
            platelist = [n for n in i if n % 3 == 2]
            print platelist
            print i
        #print int(''.join(map(str, sortedPlates)))

bunnies(plates)
