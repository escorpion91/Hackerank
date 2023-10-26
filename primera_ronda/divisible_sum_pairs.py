# def divisibleSumPairs(k, ar):
#     count = 0
#     for i in ar:
#         for j in ar:
#             if i < j and (i + j) % k == 0:
#                 count += 1
#     return count


# print(divisibleSumPairs(3, [1, 3, 2, 6, 1, 2]))

# MI APROACH, O SEA EL DE ARRIBO, FALLO EN UNOS 6 TEST CASES


def divisibleSumPairs(n, k, ar):
    count = 0

    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count


# Siempre j tiene que ser un index mas a ala derecha y sus valores deben sumar multiplos de 5
