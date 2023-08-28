numero1 = int(input("Ingresar un numero : "))
numero2 = int(input("Ingresar otro  numero : "))
numero3 = int(input("Ingresar el ultimo numero : "))

if(numero1 > numero2) and (numero1>numero3):
    print("El numero mayor es : ", numero1)
if(numero2 > numero3) and (numero2>numero1):
    print("El numero mayor es : ", numero2)
if(numero3 > numero1) and (numero3>numero2):
    print("El numero mayor es : ", numero3)