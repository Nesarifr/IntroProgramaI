nota = float(input("Ingresa una nota :"))

if(nota>0 and nota <=3):
    print("Reprobado")
elif(nota>=4 and nota <=6):
    print("Debe rendir examen final")
elif(nota>=7 and nota<=10):
    print("Eximido")
else:
    print("La nota es invalida")