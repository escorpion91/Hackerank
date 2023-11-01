try:
    monto = int(input("Ingresar monto:"))

    ginecologia = round(monto * 0.40)
    traumatologia = pediatria = round(monto * 0.30)

    print('traumatología: ', traumatologia, '$')
    print('ginecología: ', ginecologia, '$')
    print('pediatría: ', pediatria, '$')
except ValueError:
    print("Ha ingresado el valor incorrectamente")
