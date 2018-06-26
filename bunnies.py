from itertools import combinations

plates = [8, 5, 1, 8, 3, 4]

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
            if n % 3 == 1:
                sortedPlates.pop(n)
        print int(''.join(map(str, sortedPlates)))
bunnies(plates)
