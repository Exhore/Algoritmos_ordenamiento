def insertionSort(list=[]):

    """ Insertion Sort - Para pequeños sets de datos.
    - Si el array está ordenado previamente pero al revés, no debería de usar este algoritmo.
    - Debe de tener un contenido heterógeno.
    - Muy útil si la lista ya viene mínimamente ordenada desde un principio(input)

     """

    for i in range(1, len(list)):
        key = list[i]
        j = i-1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key

    return list

print(insertionSort([123189,832929,12,100,32]))
