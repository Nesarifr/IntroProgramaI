primerNota = float(input("Ingresa la primer nota: "))
segundaNota = float(input("Ingresa la segunda nota: "))

promedio = (primerNota + segundaNota) / 2

print("El promedio de las notas es : ", promedio)

if promedio>7:
    print("Aprobado")
else:
    print("Desaprobado")