weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print("Alle dagen van de week zijn " + ', '.join(weekdagen))

print("De werkdagen zijn " + ', '.join(weekdagen[0:5]))

print("De weekenddagen zijn " + ', '.join(weekdagen[5:7]))

print("De werkdagen in omgekeerde volgorde zijn " + ', '.join(weekdagen[4::-1]))

print("De weekenddagen in omgekeerde volgorde zijn " + ', '.join(weekdagen[7:4:-1]))    