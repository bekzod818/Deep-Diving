def linear_search(arr: list, number: int) -> int:
    for index in range(len(arr)):
        if arr[index] == number:
            return index
    return -1


answer = linear_search([1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99], 45)
print(answer)
