def bubble_sort(array: list) -> list:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array


result = bubble_sort([5, 2, 7, 0, 3, 6, 1, 4])
print(result)
