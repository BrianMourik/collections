#yooooooo
import random

spellist = ["Monopoly", "Yathzee", "Bridge", "Poker", "Pesten", "Mens erger je niet", "Cluedo"]

def spelprogramma(spellist, minimum, maximum):
    willekeurig = []

    for i in range(random.randint(minimum,maximum)):
        rngspel = random.randint(0,len(spellist)-1)
        willekeurig.append(spellist[rngspel])

    return willekeurig

print(spelprogramma(spellist,6,12))