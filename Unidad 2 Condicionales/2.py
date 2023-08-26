edad = int(input("¿Cuantos años tenes?: "))
distancia = int(input("¿A cuantos km esta del centro de votacion?: "))

if(edad > 70):
    print("Esta exento de ir a votar, tiene mas de 70 años")
elif(edad < 18):
    print("Esta exento de ir a votar, tiene menos de 18 años")
elif(distancia >500):
    print("Esta exento de ir a votar, esta a mas de 500km de distancia")
else:
    print("Tiene que ir a votar! Gracias.")
