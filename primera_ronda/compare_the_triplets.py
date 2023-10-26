def compareTriplets(a, b):

    alice = 0
    bob = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]


lista1 = [1, 2, 3]
lista2 = [3, 2, 1]


print(compareTriplets(lista1, lista2))
