

def migratoryBirds(arr):
    lista = [0] * len(arr)

    for i in range(len(arr)):
        lista[arr[i]] += 1

    return lista.index(max(lista))

    # La idea de esta solucion es, crear una lista de ceros.
    # La lista tendra igual items ceros como items tiene el array que te pasen.
    # Se correra un for loop por aca item en el array.

    # La logica es la siguiente: si por ejemplo, el primer index del array es un 3, le sumare un +1 al item 3 de mi lista de ceros
    # Es decir, hare un contador, cuya relacion es el valor del index de array atado al index de tu nueva lista
    # Si tu index 0 tiene valor de 4, pues le sumo a mi index 4 un +1
    # Si me vuelvo a encontrar a otro valor 4 en otro index tuyo, igual le summare a mi index 4
    # Mi lista se veria [0,0,0,1,0]
    # A fin de cuentas no estoy append ni pusheando un numero al otro, si no que mi lista basicamente es un contador.
    # Despues uso la funcion max para ver cual es el numero mas alto y saco el index de ese max.
