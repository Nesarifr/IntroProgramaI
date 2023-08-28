numero1 = int(input("Ingresar un numero : "))
numero2 = int(input("Ingresar otro  numero : "))
numero3 = int(input("Ingresar el ultimo numero : "))

nota = (numero1 + numero2 + numero3)/3

if(nota>0 and nota <=3):
    print("Reprobado, su promedio es: ", nota)
elif(nota>=4 and nota <=6):
    print("Debe rendir examen final, su promedio es: ", nota)
elif(nota>=7 and nota<=10):
    print("Eximido, su promedio es: ", nota)
else:
    print("La nota es invalida")