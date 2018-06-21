from itertools import combinations

plates = [1, 8, 8, 2]

def bunnies(plates):
    if not len(plates) < 9:
        print 'pls add plates'
    for n in range(1, len(plates)):
        for i in combinations(plates, 2):
            print (i)

bunnies(plates)
