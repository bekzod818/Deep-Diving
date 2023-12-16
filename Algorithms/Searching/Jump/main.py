from math import isqrt


def jump_search(array: list, target: int) -> int:
    array_size = len(array)
    block_size = isqrt(array_size)
    current_index = block_size
    previous_index = 0

    while array[min(current_index, array_size)] < target:
        previous_index = current_index
        current_index += block_size

        if previous_index >= array_size:
            return -1

    for index in range(previous_index, min(current_index, array_size)):
        if array[index] == target:
            return index

    return -1


result = jump_search([1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99], 23)
print(result)
