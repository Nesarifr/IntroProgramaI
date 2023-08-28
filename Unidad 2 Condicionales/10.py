consumo = float(input("Ingrese el consumo en Kw: "))
tarifa = float(480)
valorKw = 25.5
impuestos = 78


consumo = consumo - 200
tarifa = tarifa + (consumo * 25.5 ) + 78

print("La tarifa es: ", tarifa)