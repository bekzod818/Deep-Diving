from random import choice


def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    value = choice(array)

    equal = []
    left = []
    right = []

    for item in array:
        if item < value:
            left.append(item)
        elif item > value:
            right.append(item)
        else:
            equal.append(item)

    return quick_sort(left) + equal + quick_sort(right)


arr = [2, 1, -3, 0, 3, -4, 5, -1, 9, 7, -5]
print(quick_sort(arr))


def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    pivot_index = len(array) // 2
    pivot = array[pivot_index]

    left = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


arr = [2, 1, -3, 0, 3, -4, 5, -1, 9, 7, -5]
print(quick_sort(arr))
