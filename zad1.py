suma = 0
brojac = 0


broj = input("Unijeti broj: ")
if broj != "=":
    broj = int(broj)

while broj!= "=":
    if int(broj) % 5 != 0 and int(broj) % 3 == 0:
        suma += broj
        brojac += 1


    broj = input("Unijeti broj: ")



print("Arithmeticka sredina je: " + str(suma/brojac) )