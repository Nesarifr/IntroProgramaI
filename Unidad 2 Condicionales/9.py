dniInput = int(input("ingrese un dni: "))

listaDnis = [30612453 , 23763290, 21448503, 34582048, 15364857]

for dni in listaDnis:
    if dni == dniInput:
        print("Existe este dni en la lista")
        break
