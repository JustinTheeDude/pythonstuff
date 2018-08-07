from itertools import combinations, permutations
import pprint

plates = [8, 5, 1, 8, 3, 4]

def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for i in combinations(plates, len(plates)):
        sortedPlates = sorted(plates, key=int, reverse=True)
        sumOfPlates = sum(plates)
        newPlates = list(permutations(sortedPlates, 2))
        sumplate = map(sum, newPlates)
        pprint.pprint(sumplate)
        pprint.pprint(newPlates)
        if sumplate % 3 == 1:
            check(sumplate)
        print int(''.join(map(str, sortedPlates)))
bunnies(plates)
