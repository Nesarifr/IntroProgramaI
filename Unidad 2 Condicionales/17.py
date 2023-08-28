a = float(input("Ingrese el primer coeficiente a: "))
b = float(input("Ingrese el segundo coeficiente b: "))

if(a==0):
    if(b==0):
        print("Todos los numeros reales son solucion.")
    else:
        print("No tiene solucion")    
elif(b==0):
    print("Solucion unica, es cero.")
else:
    solucion = b / a
    print("La solucion es : ", solucion)
    