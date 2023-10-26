try:
    llantas = int(input("Ingrese cuántas llantas compró? "))
    if llantas < 5 and llantas > 0:
        precio = 800 * llantas
        print("El total de llantas que llevará es de: ", llantas,
              " Y el valor a pagar es de: $", precio)
    elif llantas >= 5:
        precio = 700 * llantas
        print("El total de llantas que llevará es de: ", llantas,
              " Y el valor a pagar es de: $", precio)
    else:
        print("Ha ingresado el valor incorrectamente")
except ValueError:
    print("Ha ingresado el valor incorrectamente")
