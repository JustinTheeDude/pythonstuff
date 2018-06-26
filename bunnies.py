from itertools import combinations

plates = [4, 4, 1, 8, 3, 6]

def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for i in combinations(plates, len(plates)):
        sortedPlates = sorted(plates, key=int, reverse=True)
        sumOfPlates = sum(plates)
        for n in sortedPlates:
            if sumOfPlates % 3 == 0:
                print 'cool'
                break
            if n % 3 == 2:
                sortedPlates.remove(n)
        print int(''.join(map(str, sortedPlates)))
bunnies(plates)
