from itertools import combinations
plates = [8, 5, 1, 8, 3, 4]


def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for i in xrange(len(plates), -1, -1):
        sortedPlates = sorted(plates, key=int, reverse=True)
        platestring = ''.join(map(str, sortedPlates))
        sumOfPlates = sum(plates)
        if sumOfPlates % 3 == 0:
            print 'good'
        if sumOfPlates % 3 == 2:
            for comb in combinations(platestring, i):
                platelist = [n for n in comb if n % 3 == 2]
                print platelist
                return
        # print int(''.join(map(str, sortedPlates)))


bunnies(plates)
