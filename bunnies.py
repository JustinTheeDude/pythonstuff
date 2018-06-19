plates = [1, 8, 8, 2]

def bunnies(plates):
    if len(plates) < 9:
        print 'pls add plates'
    else:
        for i in range(0, plates):
            print([i])
        plates = sum(plates)
        if plates % 3 == 0:
            print plates
        else:
            print 'bad'
bunnies(plates)
