def breakingRecords(scores):
    min_count = max_count = 0

    min_score = max_score = scores[0]

    for i in range(1, len(scores)):
        if min_score < scores[i]:
            min_score = scores[i]
            min_count += 1
        elif max_score > scores[i]:
            max_score = scores[1]
            max_count += 1

    return [max_count, min_count]


# EN EL DE ARRIBA, LA RAZON POR LA CUAL HACE LO DE RANGE Y LEN ES POR QUE DE ESA MANERA DE UNA COMPARA EL SEGUNDO INDEX CON EL PRIMERO.
# en cambio abajo yo si hago una comparacion innecesaria de max, que es el primer index con el primrr index

# def breakingRecords(scores):
#     max_count = 0
#     min_count = 0

#     max = scores[0]
#     min = scores[0]

#     for score in scores:
#         if score > max:
#             max_count += 1
#             max = score
#         elif score < min:
#             min_count += 1
#             min = score

#     return [max_count, min_count]
