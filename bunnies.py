from itertools import combinations

plates = [1, 8, 8, 2]

def bunnies(plates):
    if not len(plates) < 9:
        print 'pls add plates'

    for i in combinations(plates, ):
        print (i)

bunnies(plates)
