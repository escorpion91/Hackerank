
try:
    persona_1 = int(input('Cuanto invirtio la 1era persona? '))
    persona_2 = int(input('Cuanto invirtio la 2da persona? '))
    persona_3 = int(input('Cuanto invirtio la 3da persona? '))

    monto_total = persona_1 + persona_2 + persona_3

    porcentaje_1 = round((persona_1 / 100) * monto_total)
    porcentaje_2 = round((persona_2 / 100) * monto_total)
    porcentaje_3 = round((persona_3 / 100) * monto_total)

    print(
        f"los porcentajes son {porcentaje_1} %, {porcentaje_2} % y {porcentaje_3} % respectivamente")
except ValueError:
    print("Ha ingresado el valor incorrectamente")
