def selection_sort(array: list) -> list:
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


result = selection_sort([4, 2, 5, 1, 3, 6, 0, 7])
print(result)
