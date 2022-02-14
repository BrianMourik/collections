import random
kleuren = ["oranje", "blauw", "groen", "bruin"]

hoeveel = int(input("Hoeveel M&M's wilt u in een zak: "))

def zakvuller(aantal):
    zak = []

    for i in range(hoeveel):
        rng = random.randint(0,len(kleuren)-1)
        zak.append(kleuren[rng])

    return zak

print(zakvuller(6))