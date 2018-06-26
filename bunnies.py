from itertools import combinations

plates = [1, 8, 8, 2]

def bunnies(plates):
    if not len(plates) <= 9:
        print 'pls add plates'
    for n in range(0, len(plates)+1):
        for i in combinations(plates, len(plates)):
           sortedPlates = sorted(plates, key=int, reverse=True)
           sumOfPlates = sum(plates)
           if sumOfPlates % 3 == 0:
               print 'cool'
    print int(''.join(map(str, sortedPlates)))
bunnies(plates)
