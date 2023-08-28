anio= int(input("Ingrese un año:"))

if(anio %4 ==0 and anio%100==0 and anio%400==0):
    print("Es un año bisiesto!")
else:
    print("No es una año bisiesto!")