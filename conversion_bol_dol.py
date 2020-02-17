"""
E-P-S
Entradas:cant_bol,tasa_cambio:real
Proceso:
 cant_dolares=cant_bol/tasa_cambio
Salida:
cant_dolares:real
Diseño de la solución algoritmica
algoritmo conver_bol_dolar
var
real:cant_bol,tasa_cambio,cant_dolares
inicio
  escribir("Ingrese la cantidad en bolivares: ")
  leer(cant_bol)
  escribir("Ingrese la tasa de cambio: ")
  leer(tasa_cambio)
  cant_dolares=cant_bol/tasa_cambio
  escribir("Cantidad en dolares es: ",cant_dolares)
fin algoritmo  conver_bol_dolar
"""
#Etapa de codificación
cant_bol=float(input("Ingrese la cantidad en bolivares:"))
tasa_cambio=float(input("Ingrese la tasa de cambio: "))
cant_dolares=cant_bol/tasa_cambio
print("Cantidad en dolares es: ",cant_dolares)