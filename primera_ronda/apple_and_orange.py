# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     casa = list(range(s, t + 1))
#     arbol_manzanas = a
#     arbol_naranjas = b

#     count_manzanas = 0
#     count_naranjas = 0

# for apple in apples:
#         ubicacion = arbol_manzanas + apple
#         if ubicacion in casa:
#             count_manzanas += 1

#     for orange in oranges:
#         ubicacion = arbol_naranjas + orange
#         if ubicacion in casa:
#             count_naranjas += 1

#     return count_manzanas, count_naranjas


def countApplesAndOranges(s, t, a, b, apples, oranges):

    count_manzanas = count_naranjas = 0

    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            count_manzanas += 1

    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            count_naranjas += 1

    print(count_manzanas)
    print(count_naranjas)


print(countApplesAndOranges(7, 9, 6, 12, [2, -5-5], [5, -5, 5]))
