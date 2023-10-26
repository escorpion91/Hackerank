def staircase(n):
    for i in range(n):
        espacio = " " * (n - (i + 1))
        numeral = "#" * (i + 1)
        print(espacio + numeral)


print(staircase(6))
