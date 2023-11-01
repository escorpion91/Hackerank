
numeros = []

while True:
    respuesta = input(
        "Si deseas salir escribe 'salir'! Ahora, dime un numero! ")
    if respuesta == "salir":
        break
    try:
        respuesta2 = int(respuesta)
        if isinstance(respuesta2, int):
            numeros.append(respuesta)
        else:
            print("Valor incorrecto")
    except ValueError:
        pass


numeros.sort()

numero_menor = (numeros[0])
numero_mayor = (numeros[-1])

print('Tu numero menor es ', numero_menor)
print('Tu numero mayor es ', numero_mayor)
