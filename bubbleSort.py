def metodo_burbuja(numeros):
    """ Lista de números para ordenar. El método burbuja recorre la posición actual con un for
    y una posición superior para comparar entre ellas si el índice posterior es mayor que el anterior. Si se cumple
    el caso de que el índice actual es mayor que el siguiente, debe de swapear 'posiciones' (más bien, valores).

    El for tiene un límite, y es que una vez recorrido por primera vez la lista, ya para. La lista devolverá un pequeño orden,
    pero no definitivo. Es por ello que hay que hacer un while hasta que consiga ordenar completamente la lista."""

    swap = True

    while swap:

        swap = False

        for pos in range (0, len(numeros) - 1):
            current_number = numeros[pos]
            next_number = numeros[pos + 1]

            if current_number > next_number:
                swap = True


                numeros[pos] = next_number
                numeros[pos + 1] = current_number

    return print(numeros)





## version alternativa con 2 bucles




lista = [12,50,300,1200,10,1]

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j] > lista[i]:
            temporal = lista[j]
            lista[j] = lista[i]
            lista[i] = temporal
print(lista)