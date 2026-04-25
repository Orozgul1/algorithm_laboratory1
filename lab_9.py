# Функция пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # обмен элементов
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Функция двоичного поиска
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print("Элемент найден! Индекс:", mid)
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("Элемент не найден")



numbers = [5, 2, 9, 1, 7]

print("Исходный список:", numbers)


sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)

binary_search(sorted_numbers, 7)