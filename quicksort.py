def quick_sort(numbers):
    """ Comprueba si la longitud de la lista es menor a 2, y si sí, devuelve.
    El algoritmo utiliza recursividad. Crea 3 listas y una variable pivote, que siempre es
    el último índice del array numbers. Comprueba, y si es o no es, añade al array que debe ser.
    Por último, ordena esos mismos arrays haciendo recursividad."""

    if len(numbers) < 2:
        return numbers

    pivot = numbers[-1]

    small, equal, large = [],[],[]

    for number in numbers:

        if number < pivot:
            small.append(number)

        if number == pivot:
            equal.append(number)

        if number > pivot:
            large.append(number)

    return quick_sort(small) + equal + quick_sort(large)

