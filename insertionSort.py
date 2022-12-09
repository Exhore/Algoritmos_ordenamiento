def insertionSort(list=[]):

    """ Insertion Sort - Para pequeños sets de datos.
    - Si el array está ordenado previamente pero al revés, no debería de usar este algoritmo.
    - Debe de tener un contenido heterógeno.

     """

    for i in range(1, len(list)):
        key = list[i]
        j = i-1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    return list

# versión alternativa

"""
def insertionSortAlt(list=[]):

    number = len(list)
    for i in range(1, number):
        x = number[i]
        j = i
        while j >= 1 and number[j - 1] > number:
            number[j] = number[j - 1]
            j -= 1
        number[j] = x
    return number """

