personage = input("Creeër een eerste personage ")
plaats = input("ZOek een goede plaats waar het verhaal start ")
personage_2 = input("Iemand van wie je fan bent ")


print("Er was eens een " + personage)
print("die leefde heel heel diep in het/de " + plaats)
print("Op een niet zo bijzondere dag kwam een " + personage_2 +  " en ")

lijst = input("Vul hier de boodschappen in: ")
boodschappen = lijst.split(",")
print( personage_2 + " wilde naar de winkel om " + lijst + ". ")
print("Eenmaal aangekomen in de winkel, vergat hij het tweede item op zijn/ haar lijstje!" + "Wat was dat nu ook weer?")

for item in boodschappen:
    print(boodschappen[1])


