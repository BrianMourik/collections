import random
kleuren = ["oranje", "blauw", "groen", "bruin"]

hoeveel = int(input("Hoeveel M&M's wilt u in een zak: "))

def zakvuller(hoeveel):
    zak = {

    }

    for i in range(hoeveel):
        rng = random.randint(0,len(kleuren)-1)


        if kleuren[rng] not in zak:
            zak[kleuren[rng]] = 0
        
        count = zak.get(kleuren[rng])
        count += 1

        zak.update({kleuren[rng] : count})

    return zak

print(zakvuller(hoeveel))