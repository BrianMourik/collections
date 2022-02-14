listone = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listtwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

counter = 0
print(" ")
print("--------------------")
print("add list")

while counter != 10:
    print(str(listone[counter]) + " + " + str(listtwo[counter]) + " = " + str(listone[counter] + listtwo[counter]))
    counter = counter + 1

counter = 0
print(" ")
print("--------------------")
print("subtract list")

while counter != 10:
    print(str(listone[counter]) + " - " + str(listtwo[counter]) + " = " + str(listone[counter] - listtwo[counter]))
    counter = counter + 1

counter = 0
print(" ")
print("--------------------")
print("multiply list")

while counter != 10:
    print(str(listone[counter]) + " * " + str(listtwo[counter]) + " = " + str(listone[counter] * listtwo[counter]))
    counter = counter + 1

counter = 0
print(" ")
print("--------------------")
print("divide list")

while counter != 10:
    print(str(listone[counter]) + " / " + str(listtwo[counter]) + " = " + str(listone[counter] / listtwo[counter]))
    counter = counter + 1