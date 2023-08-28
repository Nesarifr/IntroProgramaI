numero1 = int (input("Primer entero : "))
numero2 = int (input("Segundo entero : "))

auxiliar = numero1

if(numero1 < numero2):
    numero1 = numero2
    numero2 = auxiliar

print("El orden de mayor a menor es : ", numero2, numero1)