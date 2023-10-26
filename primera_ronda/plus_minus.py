arr = [-4, 3, -9, 0, 4, 1]


def plusMinus(arr):
    total = len(arr)
    positivos = 0
    negativos = 0
    nulo = 0

    for i in arr:
        if i > 0:
            positivos += 1
        elif i < 0:
            negativos += 1
        else:
            nulo += 1
    print(positivos/total)
    print(negativos/total)
    print(nulo/total)


plusMinus(arr)
