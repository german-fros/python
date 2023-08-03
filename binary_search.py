def binary_search(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 7

result = binary_search(array, x, 0, len(array) - 1)

if result != -1:
    print(f'O elemento {x} está presente no índice {result}.')

else:
    print(f'Não foi encontrado o elemento {x}.')
