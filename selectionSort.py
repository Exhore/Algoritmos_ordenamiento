def selection_sort(numbers):
    """ Implementa el algoritmo selection sort """

    for pos_market in range(0, len(numbers) - 1):

        for pos in range(pos_market + 1, len(numbers)):

            if numbers[pos_market] > numbers[pos]:
                numbers[pos_market], numbers[pos] = numbers[pos], numbers[pos_market]

    return numbers

numbers = selection_sort([6,8,7,1])
print(numbers)