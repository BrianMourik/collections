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

        sort_zak = sorted(zak.items(), key=lambda x: x[1], reverse=True)

    for o in sort_zak:
        print(o[0], o[1])

zakvuller(hoeveel)