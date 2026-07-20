#Calcular precio con descuento
precio = float(input("Ingrese el precio original: "))

if precio <= 100:
    descuento = 0.10
elif precio <= 200:
    descuento = 0.20
elif precio <= 500:
    descuento = 0.20
else:
    descuento = 0.25

precio_final = precio - (precio * descuento)
print ("El precio con descuento es: ", precio_final)