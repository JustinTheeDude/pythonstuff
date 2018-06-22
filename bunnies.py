from itertools import combinations

plates = [1, 8, 8, 2]

def bunnies(plates):
    if not len(plates) < 9:
        print 'pls add plates'
    for i in combinations(plates, len(plates)):
       sortedPlates = sorted(plates, key=int, reverse=True)
       sumOfPlates = sum(plates)
       print key 
       if sumOfPlates % 3 == 0:
           print 'Ay ay captain'
bunnies(plates)
